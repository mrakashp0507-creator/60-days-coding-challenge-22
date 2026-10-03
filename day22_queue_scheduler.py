# Day 22 - Queues & Scheduling Systems
# Theme Park Ride Scheduler
#
# Normal visitors follow FIFO.
# VIP visitors are processed before normal visitors.

from collections import deque


class RideScheduler:

    def __init__(self):
        self.normal_queue = deque()
        self.vip_queue = deque()

    # Add visitor to the appropriate queue
    def add_visitor(self, name, vip=False):

        if vip:
            self.vip_queue.append(name)
            print(f"VIP JOINED  -> {name}")
        else:
            self.normal_queue.append(name)
            print(f"NORMAL JOINED -> {name}")

        self.display_queues()

    # Process next visitor
    def process_next(self):

        if self.vip_queue:
            visitor = self.vip_queue.popleft()
            print(f"\n🎟️ PROCESSING VIP -> {visitor}")

        elif self.normal_queue:
            visitor = self.normal_queue.popleft()
            print(f"\n🎟️ PROCESSING NORMAL -> {visitor}")

        else:
            print("\nNo visitors waiting.")
            return

        self.display_queues()

    # Display current queue state
    def display_queues(self):

        print("\n-----------------------------")
        print("VIP Queue:")
        print(list(self.vip_queue))

        print("Normal Queue:")
        print(list(self.normal_queue))
        print("-----------------------------")


# ============================================================
# MAIN PROGRAM
# ============================================================

print("======================================")
print("     FUTURISTIC THEME PARK")
print("       RIDE SCHEDULER")
print("======================================")

scheduler = RideScheduler()

# Visitors joining the park

scheduler.add_visitor("Akash")
scheduler.add_visitor("Rahul")
scheduler.add_visitor("Priya")

# VIP visitors

scheduler.add_visitor("Arjun", vip=True)
scheduler.add_visitor("Meena", vip=True)

print("\n=== PROCESSING VISITORS ===")

scheduler.process_next()
scheduler.process_next()
scheduler.process_next()
scheduler.process_next()
scheduler.process_next()
scheduler.process_next()

print("\n=== SCHEDULING COMPLETE ===")
