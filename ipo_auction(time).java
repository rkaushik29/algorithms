public class StockDistribution {

    //List info -  <uid,nostockWant,bidPrice,ts>
    public int StockDistribution(List<List<Integer>> list, int availStocks){


        PriorityQueue<List<Integer>> pq = new PriorityQueue<>(new Comparator<List<Integer>>() {
            @Override
            public int compare(List<Integer> o1, List<Integer> o2) {

                int comp = o2.get(2)-o1.get(2);

                if(comp==0){
                    return o1.get(3)-o2.get(3);
                }
                else{
                    return comp;
                }
            }
        });


        pq.addAll(list);

        List<List<Integer>> temp= new ArrayList<>();
        int noStocks = availStocks;

        while(!pq.isEmpty() && noStocks>0){

            List<Integer> pollVal =pq.poll();
            temp.add(pollVal);

            while(!pq.isEmpty() && (pollVal.get(2).equals(pq.peek().get(2)))) {

                pollVal = pq.poll();
                temp.add(pollVal);
                noStocks -= 2;

            }

            if(temp.size()==1){
                 noStocks-=pollVal.get(1);

                 if(noStocks<pollVal.get(1))
                     pq.add(temp.get(0));
            }
            else{

                for(List<Integer> li: temp) {

                    if (li.get(1) > 1)
                        pq.add(Arrays.asList(li.get(0), li.get(1) - 1, li.get(2), li.get(3)));

                }
            }
            temp.clear();

        }


        return pq.size();

    }
}