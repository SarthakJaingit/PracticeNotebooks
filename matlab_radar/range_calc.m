c = 3* 10^8; 
d_res = 1; 
max_range = 300; 

B_sweep = c / 2 * d_res

T_chirp = 5.5 * 2 * max_range / c; 

beat_freqs = [0, 1.1e6, 13e6 , 24e6]; 
R = c * T_chirp * beat_freqs / (2 * B_sweep); 

disp(R); 
