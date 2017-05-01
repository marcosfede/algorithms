from functools import reduce


def list_flatten(l):
    def flatten(pv, cv):
        if not isinstance(cv, list):
            return pv + [cv]
        else:
            return pv + list_flatten(cv)
    return reduce(flatten, l, [])


print(list_flatten([2, 1, [3, [4, 5], 6], 7, [8]]))
print('output should be [2, 1, 3, 4, 5, 6, 7, 8]')

# more procedural option

# def list_flatten(l):
#     pv = []
#     for cv in l:
#         if not isinstance(cv, list):
#             pv = pv + [cv]
#         else:
#             pv = pv + list_flatten(cv)
#     return pv

# stack version

# public static List<Integer> flatten(List<NestedList> l) {
# List<Integer> main = new ArrayList<Integer>();
# Stack<List<NestedList>> stack = new Stack<List<NestedList>>();
# Stack<Integer> indexes = new Stack<Integer>();
# stack.add(l);
# indexes.add(0);
# while (true) {
# if (stack.isEmpty())
# break;
# int index1 = indexes.pop();
# l = stack.pop();
# for (int i = index1; i < l.size(); i++) {
# NestedList n = l.get(i);
# if (n.isInteger()) {
# main.add(n.value);
# } else {
# stack.add(l);
# indexes.add(i+1);
# l = n.list;
# stack.add(l);
# indexes.add(0);
# break;

# }
# }
# }

# return main;
# }
