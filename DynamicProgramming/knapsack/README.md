Suppose you woke up on a mysterious island and there are numerous valuable items on the island. You have a knapsack (a bag) with you which you can use to take back these items with you. But, the problem is there is a limit to the weight that your knapsack can carry. So, our questions would be what is the best way to cram items into our knapsack to maximize the overall value of items that you can carry back with you? 

(*How can we maximize the overall value of the cargo given their is a weight restriction on the method of transport?*)

We have n items with their weights wi and values vi. We are given the total capacity of the knapsack, W.

For example,

Consider items with weights w = [4, 9, 3, 5, 7]

and their corresponding values v = [10, 25, 13, 20, 8]

The knapsack that we have cannot carry weight more than W = 10

---

Variations: 

1. Unbounded knapsack

  - In the case of the unbounded knapsack, we have unlimited copies of all the items.

2. 0-1 knapsack

  - In the case of the 0-1 knapsack, we have only one copy of each item. We can either chose a given item or we don't choose an item to maximize the value of our knapsack. We will look more into this in the next section.