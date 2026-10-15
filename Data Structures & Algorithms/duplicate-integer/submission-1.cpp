class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int v_length = nums.size();
        std::set<int> store;

        for(int i = 0; i < v_length; i++){
            if(store.find(nums[i]) != store.end()){
                return true;
            }
            store.insert(nums[i]);
        }
        return false;
    }
};