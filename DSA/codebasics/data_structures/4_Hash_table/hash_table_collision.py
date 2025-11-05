# Hash table with chaining
class HashTable():
    def __init__(self):
        self.MAX = 10
        self.arr  = [None for i in range(self.MAX)]

    def hash_function(self, key):
        ascii_code = 0
        for i in key:
            ascii_code += ord(i)
        h_key = (ascii_code * 2)% 10
        return h_key
    
    def __getitem__(self, key):
        h_key = self.hash_function(key)
        
        for element in self.arr[h_key]:
            if element[0] == key:
                return element[1]        
    
    def __setitem__(self, key, val):
        h_key = self.hash_function(key)
        found = False
        for idx, element in enumerate(self.arr[h_key]):
            if element[0] == key:
                self.arr[h_key][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h_key].append((key, val))

    def __delitem__(self, key):
        h_key = self.hash_function(key)
        for idx, element in enumerate(self.arr[h_key]):
            if element[0] == key:
                del self.arr[h_key][idx]
                print(f"Deleted key '{key}'.")



# Hash table with linear probing
class HashTable_2():
    def __init__(self):
        self.MAX = 10
        self.arr  = [None for i in range(self.MAX)]

    def hash_function(self, key):
        ascii_code = 0
        for i in key:
            ascii_code += ord(i)
        h_key = (ascii_code * 2) % 10
        return h_key
                
    def __getitem__(self, key):
        arr_index = self.hash_function(key)
        if self.arr[arr_index] is None:
            return None
        probe_range = self.get_probes_range(arr_index)
        for probe_index in probe_range:
            if self.arr[probe_index] and self.arr[probe_index][0] == key:
                return self.arr[arr_index][1]

    def __setitem__(self, key, val):
        arr_index = self.hash_function(key)
        if self.arr[arr_index] is None:
            self.arr[arr_index] = (key, val)
            return
        else:
            new_h = self.found_slot(key, arr_index)
            self.arr[new_h] = (key, val)

    def found_slot(self, key, arr_index):
        probe_range = self.get_probes_range(arr_index)
        for probe_index in probe_range:
            if self.arr[probe_index] is None:
                return probe_index
            if self.arr[probe_index][0] == key:
                return probe_index
        raise Exception("HashTable full.")

    def get_probes_range(self, index):
        return [*range(index, len(self.arr))] + list(range(0,index))

    def __delitem__(self, key):
        arr_index = self.hash_function(key)
        if self.arr[arr_index] is None:
            return None
        probe_range = self.get_probes_range(arr_index)
        for probe_index in probe_range:
            if self.arr[probe_index] and self.arr[probe_index][0] == key:
                del self.arr[probe_index]
                return



if __name__ == "__main__":
    # ht = HashTable()
    ht = HashTable_2()
    ht["March 6"] = 310
    ht["March 7"] = 420
    ht["March 8"] = 67
    # ht["March 17"] = 63457
    print(ht["March 6"])
    print(ht["March 17"])
    print(ht.arr)
    ht["March 6"] = 11
    print(ht.arr)
    print(ht["March 6"])
    del ht["March 6"]
    print(ht.arr)


    
