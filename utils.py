# ---------- VIDEO FUNCTION ----------
def get_video_link(topic, type_):

    base_url = "https://www.youtube.com/results?search_query="

    if type_ == "dsa":
        query = topic + " data structures and algorithms tutorial"
    else:
        query = topic + " in python programming tutorial"

    return base_url + query.replace(" ", "+")


# ---------- 100 DAY TOPICS ----------
def get_day_data(day):

    # ---------------- ALIGNED TOPICS ----------------
    topics = [

        # Day 1–10 (ARRAYS)
        ("Arrays Basics", "Python Lists", "Arrays in Java"),
        ("Array Traversal", "List Traversal", "Array Traversal in Java"),
        ("Prefix Sum", "Prefix Sum Logic", "Prefix Sum in Java"),
        ("Two Pointer", "Two Pointer Logic", "Two Pointer in Java"),
        ("Sorting", "Sorting in Python", "Sorting in Java"),
        ("Binary Search", "Binary Search Code", "Binary Search in Java"),
        ("2D Arrays", "2D Lists", "2D Arrays in Java"),
        ("Subarrays", "List Slicing", "Subarrays in Java"),
        ("Kadane Algorithm", "Max Subarray", "Kadane in Java"),
        ("Array Revision", "List Practice", "Array Practice in Java"),

        # Day 11–20 (STRINGS)
        ("Strings Basics", "String Methods", "Java Strings"),
        ("String Traversal", "Loop Strings", "String Traversal in Java"),
        ("Palindrome", "String Reverse", "Palindrome in Java"),
        ("Anagram", "Sorting Strings", "Anagram in Java"),
        ("Substring", "Slicing", "Substring in Java"),
        ("Sliding Window", "Window Logic", "Sliding Window in Java"),
        ("Hashing", "Dictionary", "HashMap in Java"),
        ("Frequency Count", "Counter", "Frequency Map in Java"),
        ("Pattern Matching", "in operator", "Pattern Matching Java"),
        ("String Revision", "String Practice", "String Practice Java"),

        # Day 21–40 (RECURSION + BACKTRACKING)
        ("Recursion Basics", "Recursion Python", "Recursion in Java"),
        ("Factorial", "Recursive Functions", "Factorial Java"),
        ("Fibonacci", "Recursion Logic", "Fibonacci Java"),
        ("Backtracking", "Backtracking Python", "Backtracking Java"),
        ("Subsets", "Subsets Python", "Subsets Java"),
        ("Permutations", "Permutations Python", "Permutations Java"),
        ("Combination Sum", "Combination Python", "Combination Java"),
        ("N Queens", "N Queens Python", "N Queens Java"),
        ("Sudoku Solver", "Sudoku Python", "Sudoku Java"),
        ("Recursion Revision", "Practice", "Recursion Practice Java"),

        # Day 41–60 (LINKED LIST + STACK + QUEUE)
        ("Linked List", "List Simulation", "Linked List Java"),
        ("Reverse Linked List", "Reverse Logic", "Reverse LL Java"),
        ("Stack", "Stack using list", "Stack Java"),
        ("Queue", "Deque", "Queue Java"),
        ("Valid Parentheses", "Stack Problem", "Stack Java"),
        ("Min Stack", "Stack Python", "Min Stack Java"),
        ("Deque", "Deque Python", "Deque Java"),
        ("Sliding Window", "Window Python", "Window Java"),
        ("LRU Cache", "Dict Logic", "LRU Java"),
        ("Stack Revision", "Practice", "Stack Practice Java"),

        # Day 61–80 (TREES)
        ("Binary Tree", "Tree Python", "Binary Tree Java"),
        ("Inorder Traversal", "DFS", "Inorder Java"),
        ("Preorder Traversal", "DFS", "Preorder Java"),
        ("Postorder Traversal", "DFS", "Postorder Java"),
        ("Level Order", "BFS", "Level Order Java"),
        ("BST", "BST Python", "BST Java"),
        ("LCA", "Tree Logic", "LCA Java"),
        ("Diameter", "Tree Logic", "Diameter Java"),
        ("Path Sum", "Tree Problem", "Path Sum Java"),
        ("Tree Revision", "Practice", "Tree Practice Java"),

        # Day 81–100 (GRAPHS + DP)
        ("Graph Basics", "Graph Python", "Graph Java"),
        ("BFS", "Queue", "BFS Java"),
        ("DFS", "Recursion", "DFS Java"),
        ("Cycle Detection", "Graph Logic", "Cycle Java"),
        ("Topological Sort", "Graph Algo", "Topo Java"),
        ("Dijkstra", "Graph Algo", "Dijkstra Java"),
        ("Union Find", "DSU Python", "DSU Java"),
        ("DP Basics", "DP Python", "DP Java"),
        ("Knapsack", "DP Problem", "Knapsack Java"),
        ("Final Revision", "Practice", "Final Practice Java"),
    ]

    # repeat for 100 days
    dsa, python, java = topics[(day - 1) % len(topics)]

    return {
    "dsa": {
        "topic": dsa,
        "video": f"https://www.youtube.com/results?search_query={dsa.replace(' ', '+')}+in+DSA"
    },
    "python": {
        "topic": python,
        "video": f"https://www.youtube.com/results?search_query={python.replace(' ', '+')}+python"
    },
    "java": {
        "topic": java,
        "video": f"https://www.youtube.com/results?search_query={java.replace(' ', '+')}"
    }
}

   
# ---------- LEETCODE (FULL 100 DAYS) ------
# ----
def get_leetcode_problems(day):

    problems = {

        # -------- ARRAYS (1–20) --------
        1: [{"name":"Two Sum","link":"https://leetcode.com/problems/two-sum/"},
            {"name":"Remove Duplicates from Sorted Array","link":"https://leetcode.com/problems/remove-duplicates-from-sorted-array/"}],

        2: [{"name":"Running Sum of 1d Array","link":"https://leetcode.com/problems/running-sum-of-1d-array/"},
            {"name":"Richest Customer Wealth","link":"https://leetcode.com/problems/richest-customer-wealth/"}],

        3: [{"name":"Move Zeroes","link":"https://leetcode.com/problems/move-zeroes/"},
            {"name":"Remove Element","link":"https://leetcode.com/problems/remove-element/"}],

        4: [{"name":"Find Pivot Index","link":"https://leetcode.com/problems/find-pivot-index/"},
            {"name":"Range Sum Query","link":"https://leetcode.com/problems/range-sum-query-immutable/"}],

        5: [{"name":"Maximum Subarray","link":"https://leetcode.com/problems/maximum-subarray/"}],

        6: [{"name":"Maximum Average Subarray I","link":"https://leetcode.com/problems/maximum-average-subarray-i/"}],

        7: [{"name":"Two Sum II","link":"https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"}],

        8: [{"name":"Subarray Sum Equals K","link":"https://leetcode.com/problems/subarray-sum-equals-k/"}],

        9: [{"name":"Sort Colors","link":"https://leetcode.com/problems/sort-colors/"}],

        10:[{"name":"Binary Search","link":"https://leetcode.com/problems/binary-search/"}],

        11:[{"name":"Merge Sorted Array","link":"https://leetcode.com/problems/merge-sorted-array/"}],

        12:[{"name":"Majority Element","link":"https://leetcode.com/problems/majority-element/"}],

        13:[{"name":"Rotate Array","link":"https://leetcode.com/problems/rotate-array/"}],

        14:[{"name":"Find the Duplicate Number","link":"https://leetcode.com/problems/find-the-duplicate-number/"}],

        15:[{"name":"Missing Number","link":"https://leetcode.com/problems/missing-number/"}],

        16:[{"name":"First Missing Positive","link":"https://leetcode.com/problems/first-missing-positive/"}],

        17:[{"name":"Maximum Product Subarray","link":"https://leetcode.com/problems/maximum-product-subarray/"}],

        18:[{"name":"Jump Game","link":"https://leetcode.com/problems/jump-game/"}],

        19:[{"name":"Jump Game II","link":"https://leetcode.com/problems/jump-game-ii/"}],

        20:[{"name":"Best Time to Buy and Sell Stock","link":"https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"}],

        # -------- STRINGS (21–40) --------
        21:[{"name":"Valid Palindrome","link":"https://leetcode.com/problems/valid-palindrome/"}],
        22:[{"name":"Valid Anagram","link":"https://leetcode.com/problems/valid-anagram/"}],
        23:[{"name":"First Unique Character","link":"https://leetcode.com/problems/first-unique-character-in-a-string/"}],
        24:[{"name":"Longest Common Prefix","link":"https://leetcode.com/problems/longest-common-prefix/"}],
        25:[{"name":"Find Index of First Occurrence","link":"https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/"}],
        26:[{"name":"Longest Substring Without Repeating Characters","link":"https://leetcode.com/problems/longest-substring-without-repeating-characters/"}],
        27:[{"name":"Group Anagrams","link":"https://leetcode.com/problems/group-anagrams/"}],
        28:[{"name":"String Compression","link":"https://leetcode.com/problems/string-compression/"}],
        29:[{"name":"Decode String","link":"https://leetcode.com/problems/decode-string/"}],
        30:[{"name":"Longest Palindromic Substring","link":"https://leetcode.com/problems/longest-palindromic-substring/"}],

        31:[{"name":"Palindromic Substrings","link":"https://leetcode.com/problems/palindromic-substrings/"}],
        32:[{"name":"Minimum Window Substring","link":"https://leetcode.com/problems/minimum-window-substring/"}],
        33:[{"name":"Edit Distance","link":"https://leetcode.com/problems/edit-distance/"}],
        34:[{"name":"Wildcard Matching","link":"https://leetcode.com/problems/wildcard-matching/"}],
        35:[{"name":"Regular Expression Matching","link":"https://leetcode.com/problems/regular-expression-matching/"}],
        36:[{"name":"Longest Repeating Character Replacement","link":"https://leetcode.com/problems/longest-repeating-character-replacement/"}],
        37:[{"name":"Permutation in String","link":"https://leetcode.com/problems/permutation-in-string/"}],
        38:[{"name":"Find All Anagrams in String","link":"https://leetcode.com/problems/find-all-anagrams-in-a-string/"}],
        39:[{"name":"Valid Parentheses","link":"https://leetcode.com/problems/valid-parentheses/"}],
        40:[{"name":"String Revision Practice","link":"https://leetcode.com/problemset/"}],

        # -------- RECURSION / BACKTRACKING (41–60) --------
        41:[{"name":"Subsets","link":"https://leetcode.com/problems/subsets/"}],
        42:[{"name":"Permutations","link":"https://leetcode.com/problems/permutations/"}],
        43:[{"name":"Combination Sum","link":"https://leetcode.com/problems/combination-sum/"}],
        44:[{"name":"Combination Sum II","link":"https://leetcode.com/problems/combination-sum-ii/"}],
        45:[{"name":"Subsets II","link":"https://leetcode.com/problems/subsets-ii/"}],
        46:[{"name":"Word Search","link":"https://leetcode.com/problems/word-search/"}],
        47:[{"name":"Palindrome Partitioning","link":"https://leetcode.com/problems/palindrome-partitioning/"}],
        48:[{"name":"Letter Combinations","link":"https://leetcode.com/problems/letter-combinations-of-a-phone-number/"}],
        49:[{"name":"Generate Parentheses","link":"https://leetcode.com/problems/generate-parentheses/"}],
        50:[{"name":"Backtracking Practice","link":"https://leetcode.com/problemset/"}],

        51:[{"name":"N Queens","link":"https://leetcode.com/problems/n-queens/"}],
        52:[{"name":"Sudoku Solver","link":"https://leetcode.com/problems/sudoku-solver/"}],
        53:[{"name":"Combination Sum III","link":"https://leetcode.com/problems/combination-sum-iii/"}],
        54:[{"name":"Restore IP Addresses","link":"https://leetcode.com/problems/restore-ip-addresses/"}],
        55:[{"name":"Partition to K Equal Subsets","link":"https://leetcode.com/problems/partition-to-k-equal-sum-subsets/"}],
        56:[{"name":"Permutations II","link":"https://leetcode.com/problems/permutations-ii/"}],
        57:[{"name":"Combinations","link":"https://leetcode.com/problems/combinations/"}],
        58:[{"name":"Subsets Practice","link":"https://leetcode.com/problems/subsets/"}],
        59:[{"name":"Backtracking Practice","link":"https://leetcode.com/problemset/"}],
        60:[{"name":"Backtracking Revision","link":"https://leetcode.com/problemset/"}],

        # -------- STACK / QUEUE (61–70) --------
        61:[{"name":"Valid Parentheses","link":"https://leetcode.com/problems/valid-parentheses/"}],
        62:[{"name":"Min Stack","link":"https://leetcode.com/problems/min-stack/"}],
        63:[{"name":"Next Greater Element","link":"https://leetcode.com/problems/next-greater-element-i/"}],
        64:[{"name":"Daily Temperatures","link":"https://leetcode.com/problems/daily-temperatures/"}],
        65:[{"name":"Largest Rectangle in Histogram","link":"https://leetcode.com/problems/largest-rectangle-in-histogram/"}],
        66:[{"name":"Sliding Window Maximum","link":"https://leetcode.com/problems/sliding-window-maximum/"}],
        67:[{"name":"Queue using Stacks","link":"https://leetcode.com/problems/implement-queue-using-stacks/"}],
        68:[{"name":"LRU Cache","link":"https://leetcode.com/problems/lru-cache/"}],
        69:[{"name":"Stack Practice","link":"https://leetcode.com/problemset/"}],
        70:[{"name":"Stack Revision","link":"https://leetcode.com/problemset/"}],

        # -------- TREES (71–85) --------
        71:[{"name":"Inorder Traversal","link":"https://leetcode.com/problems/binary-tree-inorder-traversal/"}],
        72:[{"name":"Preorder Traversal","link":"https://leetcode.com/problems/binary-tree-preorder-traversal/"}],
        73:[{"name":"Postorder Traversal","link":"https://leetcode.com/problems/binary-tree-postorder-traversal/"}],
        74:[{"name":"Level Order Traversal","link":"https://leetcode.com/problems/binary-tree-level-order-traversal/"}],
        75:[{"name":"Maximum Depth","link":"https://leetcode.com/problems/maximum-depth-of-binary-tree/"}],
        76:[{"name":"Diameter of Tree","link":"https://leetcode.com/problems/diameter-of-binary-tree/"}],
        77:[{"name":"Validate BST","link":"https://leetcode.com/problems/validate-binary-search-tree/"}],
        78:[{"name":"Lowest Common Ancestor","link":"https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/"}],
        79:[{"name":"Path Sum","link":"https://leetcode.com/problems/path-sum/"}],
        80:[{"name":"Serialize Tree","link":"https://leetcode.com/problems/serialize-and-deserialize-binary-tree/"}],

        81:[{"name":"Tree Practice 1","link":"https://leetcode.com/problemset/"}],
        82:[{"name":"Tree Practice 2","link":"https://leetcode.com/problemset/"}],
        83:[{"name":"Tree Practice 3","link":"https://leetcode.com/problemset/"}],
        84:[{"name":"Tree Practice 4","link":"https://leetcode.com/problemset/"}],
        85:[{"name":"Tree Revision","link":"https://leetcode.com/problemset/"}],

        # -------- GRAPHS + DP (86–100) --------
        86:[{"name":"Number of Islands","link":"https://leetcode.com/problems/number-of-islands/"}],
        87:[{"name":"Clone Graph","link":"https://leetcode.com/problems/clone-graph/"}],
        88:[{"name":"Course Schedule","link":"https://leetcode.com/problems/course-schedule/"}],
        89:[{"name":"BFS Traversal","link":"https://leetcode.com/problemset/"}],
        90:[{"name":"DFS Traversal","link":"https://leetcode.com/problemset/"}],
        91:[{"name":"Detect Cycle","link":"https://leetcode.com/problemset/"}],
        92:[{"name":"Topological Sort","link":"https://leetcode.com/problemset/"}],
        93:[{"name":"Dijkstra Algorithm","link":"https://leetcode.com/problemset/"}],
        94:[{"name":"Union Find","link":"https://leetcode.com/problemset/"}],
        95:[{"name":"Graph Practice","link":"https://leetcode.com/problemset/"}],

        96:[{"name":"Longest Increasing Subsequence","link":"https://leetcode.com/problems/longest-increasing-subsequence/"}],
        97:[{"name":"Coin Change","link":"https://leetcode.com/problems/coin-change/"}],
        98:[{"name":"House Robber","link":"https://leetcode.com/problems/house-robber/"}],
        99:[{"name":"Word Break","link":"https://leetcode.com/problems/word-break/"}],
        100:[{"name":"Climbing Stairs","link":"https://leetcode.com/problems/climbing-stairs/"}],
    }

    return problems.get(day, [{"name":"Practice","link":"https://leetcode.com/problemset/"}])
