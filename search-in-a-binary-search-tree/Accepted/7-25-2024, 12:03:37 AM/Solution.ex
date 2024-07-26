// https://leetcode.com/problems/search-in-a-binary-search-tree

# Definition for a binary tree node.
#
# defmodule TreeNode do
#   @type t :: %__MODULE__{
#           val: integer,
#           left: TreeNode.t() | nil,
#           right: TreeNode.t() | nil
#         }
#   defstruct val: 0, left: nil, right: nil
# end

defmodule Solution do
  @spec search_bst(root :: TreeNode.t | nil, val :: integer) :: TreeNode.t | nil
  def search_bst(nil, val), do: nil
  def search_bst(root, val) do
    cond do
      val == root.val -> root
      val < root.val -> search_bst(root.left, val)
      true -> search_bst(root.right, val)
    end
  end
end