int i =0;
vector<string> split_string(string);

// Complete the jumpingOnClouds function below.
int jumpingOnClouds(vector<int> c) {

   int count=0;
        int i=0;
        while(i<c.size()-1){
            if(i+2<c.size()&&c[i+2]!=1){
                count++;
                i=i+2;
            }
            else{
                count++;
                i++;
            }
        }
        return count;
}
