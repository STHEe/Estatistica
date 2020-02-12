

var DesvioQuantitico = (lst) => {
   let lista = lst.sort();
   let n = lista.length;

   let Q1 = (n + 1) / 4;
   let Q2 = ((n + 1) * 2) / 4;
   let Q3 = ((n + 1) * 3) / 4;

   return {
      Q1: Q1,
      Q2: Q2,
      Q3: Q3
   }
}

var calcularValores = (lista, Qs) => {
   let aux = new Object();
   for (const chave in Qs) {
      let value = Qs[chave];
      let valor = undefined;

      let help1 = Math.floor(value);
      let help2 = Math.ceil(value);
   
      if (help1 != help2){
         //Mais de um na mesma posição
         valor = (lista[help1] + lista[help2]) / 2
      } else {
         valor = help1; // poderia ser help2 tanto faz
      }
      aux[Qs[chave]] = valor;
   }
   return aux;
}


var Qs = null;
var teste = null;


setup = () => {
   var lst = [-50, 10, 30, 35, 25, 2 -6, -3, -16, 20, 15, 50, 26];
   
   Qs = DesvioQuantitico(lst);
   valores = calcularValores(lst, Qs);
}

draw = () => {
   createCanvas(600, 600);
   background(51);


   rect( (width / 5) )



}





