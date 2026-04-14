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

    schedule = [

        # -------- ARRAYS (1–20) --------
        ("Arrays Basics", "Python Lists Basics"),
        ("Array Traversal", "List Indexing in Python"),
        ("Insertion & Deletion", "List Methods in Python"),
        ("Prefix Sum", "For Loop in Python"),
        ("Kadane Algorithm", "Loops in Python"),
        ("Sliding Window", "List Iteration in Python"),
        ("Two Pointer", "List Comprehension in Python"),
        ("Subarrays", "Nested Lists in Python"),
        ("Sorting Basics", "Sorting in Python"),
        ("Binary Search", "Functions in Python"),
        ("Merge Arrays", "List Merge in Python"),
        ("Rotate Array", "List Slicing in Python"),
        ("Majority Element", "Counter in Python"),
        ("Peak Element", "Min Max in Python"),
        ("Missing Number", "Set in Python"),
        ("Find Duplicates", "Set Operations Python"),
        ("Subarray Sum", "Dictionary in Python"),
        ("Prefix XOR", "Bitwise in Python"),
        ("Advanced Arrays", "Practice in Python"),
        ("Array Revision", "Revision"),

        # -------- STRINGS (21–40) --------
        ("String Basics", "Strings in Python"),
        ("Palindrome Check", "String Slicing in Python"),
        ("Anagram", "Sorting Strings Python"),
        ("Frequency Count", "Dictionary Count Python"),
        ("Substring Problems", "String Loop Python"),
        ("Pattern Matching", "String Functions Python"),
        ("Longest Substring", "Sliding Window Python"),
        ("String Compression", "Replace in Python"),
        ("Reverse String", "Reverse String Python"),
        ("Valid Parentheses", "Stack in Python"),
        ("String Matching", "Find Method Python"),
        ("Count Characters", "Dict Count Python"),
        ("Regex Basics", "Regex Python"),
        ("Edit Distance", "Dynamic Programming Python"),
        ("Longest Prefix", "String Logic Python"),
        ("Advanced Strings", "Practice Python"),
        ("String Problems 1", "Practice Python"),
        ("String Problems 2", "Practice Python"),
        ("String Problems 3", "Practice Python"),
        ("String Revision", "Revision"),

        # -------- RECURSION (41–60) --------
        ("Recursion Basics", "Functions in Python"),
        ("Factorial", "Recursion Python"),
        ("Fibonacci", "Recursion Python"),
        ("Subsets", "Recursion Python"),
        ("Permutations", "Recursion Python"),
        ("Combination Sum", "Recursion Python"),
        ("Backtracking", "Advanced Functions Python"),
        ("N Queens", "Backtracking Python"),
        ("Sudoku Solver", "Backtracking Python"),
        ("Maze Problem", "Recursion Python"),
        ("Divide & Conquer", "Lambda Python"),
        ("Merge Sort", "Sorting Python"),
        ("Quick Sort", "Partition Python"),
        ("Binary Recursion", "Tree Recursion Python"),
        ("Stack Recursion", "Stack Python"),
        ("Advanced Recursion", "Practice"),
        ("Problems 1", "Practice"),
        ("Problems 2", "Practice"),
        ("Problems 3", "Practice"),
        ("Recursion Revision", "Revision"),

        # -------- TREES (61–80) --------
        ("Binary Tree Basics", "Classes in Python"),
        ("Tree Traversal", "Recursion Python"),
        ("Inorder Traversal", "DFS Python"),
        ("Preorder Traversal", "DFS Python"),
        ("Postorder Traversal", "DFS Python"),
        ("Level Order", "Queue Python"),
        ("Tree Height", "Recursion Python"),
        ("Balanced Tree", "Logic Python"),
        ("Diameter", "DFS Python"),
        ("Binary Search Tree", "OOP Python"),
        ("Insert BST", "Practice Python"),
        ("Delete BST", "Practice Python"),
        ("LCA", "Tree Python"),
        ("Path Sum", "DFS Python"),
        ("Serialize Tree", "Advanced Python"),
        ("Tree Problems 1", "Practice"),
        ("Tree Problems 2", "Practice"),
        ("Tree Problems 3", "Practice"),
        ("Tree Problems 4", "Practice"),
        ("Tree Revision", "Revision"),

        # -------- GRAPHS (81–100) --------
        ("Graph Basics", "Dictionary Python"),
        ("DFS", "Recursion Python"),
        ("BFS", "Queue Python"),
        ("Connected Components", "DFS Python"),
        ("Cycle Detection", "DFS Python"),
        ("Topological Sort", "Graph Python"),
        ("Shortest Path", "Heap Python"),
        ("Dijkstra", "Heap Python"),
        ("Union Find", "DSU Python"),
        ("Graph Problems 1", "Practice"),
        ("Graph Problems 2", "Practice"),
        ("Graph Problems 3", "Practice"),
        ("Mixed DSA 1", "Practice"),
        ("Mixed DSA 2", "Practice"),
        ("Mixed DSA 3", "Practice"),
        ("Mock Interview 1", "Practice"),
        ("Mock Interview 2", "Practice"),
        ("Weak Areas", "Revision"),
        ("Final Revision", "Revision"),
        ("Placement Ready", "Confidence"),
    ]

    dsa, py = schedule[day - 1]

    return {
        "dsa": {
            "topic": dsa,
            "video": get_video_link(dsa, "dsa")
        },
        "python": {
            "topic": py,
            "video": get_video_link(py, "python")
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
