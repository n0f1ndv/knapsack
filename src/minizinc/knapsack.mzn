int: n;
float: C;
array[1..n] of float: v;
array[1..n] of float: w;
array[1..n] of int: c;

int: m;
array[1..m, 1..m] of float: l;

array[1..n] of var 0..1: x;

constraint sum(i in 1..n)(w[i] * x[i]) <= C;

var float: total_value = sum(i in 1..n)(v[i] * x[i]);

array[1..n] of var 0..n: pos;
    constraint forall(e in 1..n)(
    sum(p in 1..n)(bool2int(pos[p]=e)) = x[e]
);
constraint forall(p in 1..n-1)(
    (pos[p] = 0 /\ pos[p+1] = 0) \/
    (pos[p] > 0 /\ pos[p+1] > 0 /\ pos[p] < pos[p+1]) \/
    (pos[p] > 0 /\ pos[p+1] = 0)
);

var float: total_penalty = sum(p in 1..n-1)(
    if pos[p] > 0 /\ pos[p+1] > 0 then
    l[c[pos[p]], c[pos[p+1]]] * (v[pos[p]] + v[pos[p+1]]) / 100.0
    else
    0.0
    endif
);

var float: final_value = total_value - total_penalty;

solve maximize final_value;

output ["Elements used: ", show(x), 
    "\n", "Value: ", show(total_value),
    "\n", "Weight: ", show(sum(i in 1..n)(w[i]*x[i])),
    "\n", "Penalty: ", show(total_penalty), 
    "\n", "Final value: ", show(final_value), "\n"];
