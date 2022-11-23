set terminal png
set output "gnuplot-helper-example.png"
set title "Emitter Count vs. Time : 201602043 \n\nTrace Source Path: /Names/Emitter/Counter"
set xlabel "Time (Seconds)"
set ylabel "Emitter Count"

set key inside
set datafile missing "-nan"
plot 
