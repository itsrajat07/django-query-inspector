from django.db import connection
import time
class QueryLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        # Clear previous queries
        connection.queries_log.clear()

        response = self.get_response(request)

        total_time = time.time() - start_time
        queries = connection.queries
        duplicate_count = len(queries) - len(set(q['sql'] for q in queries))
        print(f"Duplicate Queries: {duplicate_count}")

        print("\n====== DB QUERY REPORT ======")
        print(f"Total Queries: {len(queries)}")
        print(f"Total Request Time: {total_time:.4f}s")

        for i, query in enumerate(queries):
            print(f"{i+1}. {query['sql']} ({query['time']}s)")

        print("====== END REPORT ======\n")


        return response