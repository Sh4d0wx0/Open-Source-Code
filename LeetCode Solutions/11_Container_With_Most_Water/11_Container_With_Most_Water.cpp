class Solution {
public:
    int maxArea(vector<int>& height) {
        int start=0,end=height.size()-1;
        int ans=INT_MIN;
        while(start<end)
        {
            int res=min(height[start],height[end])*(end-start);
            ans=max(ans,res);
            if(height[start]<height[end])start++;
            else
                end--;
        }
        return ans;
    }
};