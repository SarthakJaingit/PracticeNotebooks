c = 3*10^8; 
rad_freq = 77e9; 

wave_length = c / rad_freq; 
doppler_data = [3 * 10^3, -4.5 * 10^3, 11 * 10^3, -3 * 10^3]; 

% velocity calculated from doppler effect freq changes.
velocity = (wave_length * doppler_data) / 2; 

disp(velocity); 



