# Implementation of Algorithms Using Python 

- Anagrams <br />
  A word v is an anagram of a word v if a permutation of the letters transforming w into v exits .<br />
  anagram(string st ) => list(anagrams) <br />
  input => "below elbow car thing cried cat tac act" <br />
  returns => [['below', 'elbow'], ['car'], ['thing'], ['cried'], ['cat', 'tac', 'act']] <br />

- Linear Search <br />
  linear_search(array,search_element) => Prints if search in array or not ! <br />
  Time Complexity : O(n) where n is the no of elements in array  <br />

- Binary Search <br />
  binary_search(array,search) => prints if search in array or not ! <br />
  "Needs sorted array" <br />
  Time Complexity : O(log n) where n is the no of elements in array <br />

- Jump Search <br />
  jump_search(array,search,jump=None) => prints if search in array or not ! <br />
  "Needs sorted array" <br />
  default jump = sqroot(n) <br />
  Time Complexity : O(√n) where n is the no of elements in array <br />

- Kadane's Algorithm <br />
  kadane(array) => returns three things best_sum , start_index and end_index of subarray <br />
  Time Complexity : O(n) where n is the no of elements in the array <br />

- Merge two Sorted Arrays <br />
  merge_sorted_array(array1,array2) => returns one sorted array <br />
  Time Complexity : O(n+m) where n, m are the no of elements in the array1 and array 2 <br />
  
- Selection Sort Algorithm <br />
  Sorts the array into ascending or descending order <br />
  selection_sort(array,descending = False) => return sorted array <br />
  Time Complexity : O(n^2) where n is the no of elements in the array <br />

- Insertion Sort Algorithm <br />
  Sorts the array into ascending or descending order <br />
  insertion_sort(array,descending = False) => return sorted array <br />
  Time Complexity : O(n^2) where n is the no of elements in the array <br />

- Bubble Sort Algorithm <br />
  Sorts the array into ascending or descending order <br />
  bubble_sort(array,descending = False) => return sorted array <br />
  Time Complexity : O(n^2) where n is the no of elements in the array <br />

- Dijkstras Algorithm <br />
  Uses the greedy approach to find the shorted path from source to destination in a graph <br />
  Time Complexity : O((V + E) log V) where V are the no of nodes in the graph and E are the edges of each Node. <br />