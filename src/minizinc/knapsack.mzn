int: n;
int: C;
array[1..n] of int: values; % v
array[1..n] of int: weights; % w
array[1..n] of int: categories; % c

int: m;
array[1..m, 1..m] of int: penalties; % l

array[1..n] of var 0..1: x;

constraint sum(i in 1..n)(weights[i] * x[i]) <= C;

var int: total_value = sum(i in 1..n)(values[i] * x[i]);

var int: total_penalty = 
  sum(i in 1..n-1)(
    if x[i] = 1 /\ x[i+1] = 1 /\ categories[i] != categories[i+1] then
      penalties[categories[i], categories[i+1]] * (values[i] + values[i+1]) div 100
    else
      0
    endif
  );

var int: final_value = total_value - total_penalty;

solve maximize final_value;

output ["x = ", show(x), "\n", "Total Value = ", show(total_value), "\n", "Total Penalty = ", show(total_penalty), "\n", "Final Total Value = ", show(final_value), "\n"];
