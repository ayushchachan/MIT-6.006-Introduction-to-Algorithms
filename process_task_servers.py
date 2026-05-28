import heapq


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        m = len(tasks)
        available_servers = [(servers[i], i) for i in range(n)]
        unavailable_servers = []
        heapq.heapify(available_servers)

        answer = []

        current_time = 0
        j = 0

        while j < m:
            if len(available_servers) == 0:
                current_time = unavailable_servers[0][0]
                count_newly_avail_server = 0

                while len(unavailable_servers) > 0 and unavailable_servers[0][0] == current_time:
                    server_index = heapq.heappop(unavailable_servers)[1]
                    heapq.heappush(available_servers, (servers[server_index], server_index))
                    count_newly_avail_server += 1

                count_newly_avail_server = min(count_newly_avail_server, current_time - j)
                while count_newly_avail_server > 0 and j < m:
                    task_time = tasks[j]
                    j += 1

                    assigned_server_weight, assigned_server_index = heapq.heappop(available_servers)
                    answer.append(assigned_server_index)
                    heapq.heappush(
                        unavailable_servers,
                        (current_time + task_time, assigned_server_index),
                    )

                    count_newly_avail_server -= 1
            else:
                task_time = tasks[j]

                assigned_server_weight, assigned_server_index = heapq.heappop(available_servers)
                answer.append(assigned_server_index)
                heapq.heappush(
                    unavailable_servers,
                    (current_time + task_time, assigned_server_index),
                )
                current_time += 1
                j += 1

                while len(unavailable_servers) > 0 and unavailable_servers[0][0] == current_time:
                    server_index = heapq.heappop(unavailable_servers)[1]
                    heapq.heappush(available_servers, (servers[server_index], server_index))

        return answer
