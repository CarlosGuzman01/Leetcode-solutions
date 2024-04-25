class Solution {
    public int countTestedDevices(int[] batteryPercentages) {

        int counter = 0;

        for(int i = 0; i < batteryPercentages.length; i++){
            if(batteryPercentages[i] > 0){
                counter++;

                decrementBatteries(i, batteryPercentages);

            }

        }

        return counter;
        
    }

     public static void decrementBatteries(int i, int[] batteryPercentages){
         
        for(int j = i; j < batteryPercentages.length; j++){
            if(batteryPercentages[j] == 0){
                continue;
            }

            batteryPercentages[j]--;
        }


    }


}