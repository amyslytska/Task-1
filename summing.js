function sum(list){
  let total = 0;
  for (let i = 0; i < list.length; i++) {
       total += list[i];
    }
    return total;
}

const sallary = [12000, 13000, 20000];
console.log(sum(sallary));
