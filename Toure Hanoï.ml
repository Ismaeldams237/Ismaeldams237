
let move_disque t1 t2 =
  Printf.printf "Déplacer un disque de la tige %d vers la tige %d\n" t1 t2

let rec hanoi n source target aux =
  if n > 0 then begin
    hanoi (n-1) source aux target;
    move_disque source target;
    hanoi (n-1) aux target source
  end

let solve_hanoi num_disques =
  hanoi num_disques 1 3 2 4 5 6 7

let () =
  let nombre_disques = 7 in
  Printf.printf "Pour résoudre les Tours de Hanoï avec %d disques :\n" nombre_disques;
  solve_hanoi nombre_disques ;;


