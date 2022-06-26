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