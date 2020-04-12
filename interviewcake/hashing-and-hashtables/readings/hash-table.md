# Hash Table
Data Structure

Other names:
hash, hash map, map, unordered map, dictionary

## Quick Reference
A **hash table** organizes data so you can quickly look up values for a given key.

### Strengths
- **Fast lookups.** Lookups take *O(1)* time on *average*.
- **Flexible keys**. Most data types can be used for keys, as long as they're hashable.

### Weaknesses
- **Slow worst-case lookups**. Lookups take O(n)O(n) time in the worst case.
- **Unordered**. Keys aren't stored in a special order. If you're looking for the smallest key, the largest key, or all the keys in a range, you'll need to look through every key to find it.
- **Single-directional lookups**. While you can look up the value for a given key in O(1)O(1) time, looking up the keys for a given value requires looping through the whole dataset—O(n)O(n) time.
- **Not cache-friendly**. Many hash table implementations use linked lists, which don't put data next to each other in memory.

### Runtime
|        | Average | Worst Case |
| ------ | ------- | ---------- |
| space  | O(n)    | O(n)       |
| insert | O(1)    | O(n)       |
| lookup | O(1)    | O(n)       |
| delete | O(1)    | O(n)       |

