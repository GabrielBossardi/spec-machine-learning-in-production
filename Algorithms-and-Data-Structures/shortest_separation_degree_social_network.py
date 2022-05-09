import random
import uuid
import math


class Person(object):

    def __init__(self, uid, s_type):
        self._uid = uid
        self._s_type = s_type

    def get_uid(self):
        return self._uid

    def get_s_type(self):
        return self._s_type


class FriendNetwork(object):

    def __init__(self, people_num, connections_num):
        self._people_num = people_num
        self._connections_num = connections_num
        self._graph = self._generate_graph()

    def _generate_graph(self):
        people = []

        for person_index in range(self._people_num):
            uid = str(uuid.uuid4())

            if person_index < (self._people_num // 2):
                s_type = 'female'
            else:
                s_type = 'male'

            people.append(Person(uid, s_type))

        conn_num = 0
        graph = {}
        graph_aux = {}

        while conn_num < self._connections_num:
            person, friend = random.sample(people, 2)
            person_uid = person.get_uid()
            friend_uid = friend.get_uid()

            if person_uid not in graph:
                graph[person_uid] = {
                    'this': person,
                    'friends': []
                }
                graph_aux[person_uid] = {}

            if friend_uid not in graph:
                graph[friend_uid] = {
                    'this': friend,
                    'friends': []
                }
                graph_aux[friend_uid] = {}

            if person_uid == friend_uid or friend_uid in graph_aux[person_uid]:
                continue

            graph[person_uid]['friends'].append(friend)
            graph[friend_uid]['friends'].append(person)
            graph_aux[person_uid][friend_uid] = True
            graph_aux[friend_uid][person_uid] = True
            conn_num += 1

        people_to_remove = []

        for person_uid in graph:
            friends_types = [*map(lambda p: p.get_s_type(),
                                  graph[person_uid]['friends'])]
            person_type = graph[person_uid]['this'].get_s_type()

            if ('male' not in friends_types or 'female' not in friends_types) and person_type in friends_types:  # noqa: E501
                people_to_remove.append({
                                    'person_uid': person_uid,
                                    'remove_from': graph[person_uid]['friends']
                                        })

        for person_props in people_to_remove:
            for friend in person_props['remove_from']:
                person_index = [*map(lambda friend: friend.get_uid(),
                                graph[friend.get_uid()]['friends'])].index(
                                            person_props['person_uid'])
                del graph[friend.get_uid()]['friends'][person_index]
            del graph[person_props['person_uid']]

        return graph

    def get_person_by_uid(self, uid):
        return self._graph[uid]['this']

    def _search_s_type(self, person_uid, friend_uid):
        paths = []
        explored = []
        queue = [[person_uid]]

        while queue:
            path = queue.pop(0)
            node = path[-1]
            new_path = list(path)
            node_s_type = self._graph[node]["this"]._s_type

            if node not in explored:
                neighbours = [f._uid for f in self._graph[node]['friends']
                              if f._s_type != node_s_type]

                if friend_uid in neighbours:
                    new_path.append(friend_uid)
                    paths.append(new_path)
                else:
                    for neighbour in neighbours:
                        new_path = list(path)
                        new_path.append(neighbour)
                        queue.append(new_path)

                explored.append(node)

        return [p for p in sorted(paths, key=lambda x: len(x))][0]

    def _search(self, person_uid, friend_uid):
        paths = []
        explored = []
        queue = [[person_uid]]

        while queue:
            path = queue.pop(0)
            node = path[-1]
            new_path = list(path)

            if node not in explored:
                neighbours = [*map(lambda p: p._uid,
                              self._graph[node]['friends'])]

                if friend_uid in neighbours:
                    new_path.append(friend_uid)
                    paths.append(new_path)
                else:
                    for neighbour in neighbours:
                        new_path = list(path)
                        new_path.append(neighbour)
                        queue.append(new_path)

                explored.append(node)

        return [p for p in sorted(paths, key=lambda x: len(x))][0]

    def get_separation_degree(self, search_type: str):
        search = {
           "type_1": self._search,
           "type_2": self._search_s_type
        }

        total_paths_len = 0

        for _ in range(100):
            person_uid, friend_uid = random.sample([*self._graph.keys()], 2)
            path = search[search_type](person_uid, friend_uid)
            total_paths_len += len(path) - 1

        return total_paths_len / 100


def get_average_connections(people):
    average_connections = [
                5 * people,
                int(people * math.sqrt(people)),
                int(people * people / 5)
            ]

    return average_connections


if __name__ == '__main__':

    people = [100, 1000, 10000, 100000]

    for p in people:
        print(f'\n########### {p} PEOPLE ###########')
        for c in get_average_connections(p):
            graph = FriendNetwork(p, c)

            print(f'Start search (V x E): {p} x {c}')
            shortest_path = graph.get_separation_degree(search_type='type_1')
            print(shortest_path)

            print(f'Start search alternate paths (V x E): {p} x {c}')
            shortest_path = graph.get_separation_degree(search_type='type_2')
            print(shortest_path)
