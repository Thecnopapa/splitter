import os, sys
import pandas as pd
import numpy as np




class People:
    def __init__(self, filepath):
        print(filepath)
        self.days = None
        self.people = {}
        with open(filepath, "r") as f:
            for line in f:
                if line == "" or line.startswith("#"):
                    pass
                if line.startswith(">>"):
                    if line[2:].split(":")[0].strip().lower() == "days":
                        self.days = [int(i) for i in line.split(":")[1].split(",")]
                elif line.startswith(">"):
                    name = line[1:].split(":")[0].strip()
                    if "na" in line.split(":")[1]:
                        self.people[name] = None
                        continue
                    nights = [int(i) for i in line.split(":")[1].split(",")]
                    self.people[name] = nights


    def split_price(self, value, start=None, end=None):
        value = int(value)
        start_i = 0
        if start is not None:
            start_i = self.days.index(int(start))
        end_i = len(self.days)-1
        if end is not None:
            end_i = self.days.index(int(end))
        print("Calculating for days:", self.days[start_i:end_i+1], start_i, end_i)
        shares = 0
        people_counts = {name:0 for name in self.people.keys()}       
        for n, day in enumerate(self.days[start_i:end_i]):
            print("Night: {}-{} ({}):".format(day, self.days[n+1], n), end=" ")
            for name, nights in self.people.items():
                if nights is None:
                    continue
                if n in nights:
                    people_counts[name] += 1
                    shares +=1
                    print(name, end= " ")
            print("\n")
        print("The price will be dividided in {} shares:".format(shares))
        share_price = value / shares
        [print("> {}: \t{} shares \t= {} euro:".format(name, count, round(count*share_price,2))) for name, count in people_counts.items()]


            



if __name__ == "__main__":
    print(sys.argv)
    people = People("list1.txt")
    print("DAYS:", people.days)
    print("PEOPLE:")
    [print("{}: {}".format(name, nights)) for name, nights in people.people.items()]
    price = None
    start = None
    end = None
    try:
        price = sys.argv[1]
        start = sys.argv[2]
        end = sys.argv[3]
    except:
        pass
    if price is not None:
        people.split_price(price, start, end)



