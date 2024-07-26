// https://leetcode.com/problems/create-binary-tree-from-descriptions

class Solution {
public:
    TreeNode* createBinaryTree(vector<vector<int>>& desc) {
        vector<int>vec(100001,-1);
        vector<TreeNode *>list(100001,NULL);
        for(int i=0;i<desc.size();i++){
            int p = desc[i][0];
            int c = desc[i][1];
            int left = desc[i][2];
            TreeNode *parent = list[p];
            TreeNode *child = list[c];
            if(parent==NULL){
                parent = new TreeNode(p);
                list[p] = parent;
                vec[p] = 0;
            }
            if(child==NULL){
                child = new TreeNode(c);
                list[c] = child;
            }
            vec[c] = 1;
            if(left) parent->left = child;
            else parent->right = child;
        }
        for(int i=0;i<100001;i++){
            if(vec[i]==0){
                return list[i];
            }
        }

        return NULL;
    }
};