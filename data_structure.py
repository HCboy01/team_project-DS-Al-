DEFAULT_CAPACITY = 100
class SortingDeQue:
	def __init__(self):
		self._data = [[0,2147483647] for i in range(DEFAULT_CAPACITY + 1)]
		self._rear = 0
		self._front = 0
		self._size = 0

	def __len__(self):
		return (self._size)

	def is_empty(self):
		if (self._rear - self._front == 0) :
			return (1)
		else :
			return (0)
	
	def is_full(self):
		if ((DEFAULT_CAPACITY + self._rear + 2) % (DEFAULT_CAPACITY + 1) == self._front) :
			return (1)
		else :
			return (0)
	
	def first(self):
		if (self.is_empty()) :
			raise Exception('Queue is empty')
		return (self._data[self._front])
	
	def popleft(self):
		target = self._data[self._front]
		self._data[self._front] = [0,2147483647]
		self.quick_sort(self._data)
		self._size -= 1
		return(target)
	
	def append(self, data):
		if (self.is_full()) :
			raise Exception('Queue is full')
		self._data[self._size] = data
		self.quick_sort(self._data)
		self._size += 1
		
	def quick_sort(self, arr) :
		ans = self.quick_sort_rec(arr, 0, len(arr) - 1)
		return(ans)

	def quick_sort_rec(self, arr, start, end) :
		pivot = arr[start][1]
		low = start + 1
		high = end

		while (True) :
			while low < len(arr) and pivot > arr[low][1] :
				low += 1
			while high > 0 and pivot <= arr[high][1]:
				high -= 1
			if (high < low) :
				temp = arr[start]
				arr[start] = arr[low - 1]
				arr[low - 1] = temp
				break
			else :
				temp = arr[low]
				arr[low] = arr[high]
				arr[high] = temp
			if (end != start) :
				if (high >= 1) :
					arr = self.quick_sort_rec(arr, start, high)
			if (low < end) :
				arr = self.quick_sort_rec(arr, low, end)
		return (arr)

