
close all; 

Fs = 1000; 
T = 1/Fs; 
L = 1500; 
t = (0:L-1)*T; 

% Form a signal containing a 50 Hz sinusoid of amplitude 0.7 and a 120 Hz 
% sinusoid of amplitude 1.

S = 0.7 * sin(2 * pi * 50 * t) + sin(2 * pi * 120 * t)
X = S + 2*randn(size(t));
X = abs(X)

Ns = 1500;  % let it be the same as the length of the signal

%Targets location. Assigning bin 100, 200, 300, and 700 as Targets
%  with the amplitudes of 16, 18, 27, 22.
X([100 ,200, 300, 700])=[16 18 27 22];

% figure(1);
% tiledlayout(2,1)
% nexttile
% plot(X)

T = 15
G = 4
offset = 5

threshold_cfar = zeros(Ns-(G+T+1),1);
signal_cfar = zeros(Ns-(G+T+1),1);

for i = 1:(Ns-(G+T+1))     

    % TODO: Determine the noise threshold by measuring it within 
    % the training cells
    noise_level = sum(X(i: i + T - 1))
    % TODO: scale the noise_level by appropriate offset value and take
    % average over T training cells
    threshold = offset * (noise_level / T)
    % Add threshold value to the threshold_cfar vector
    threshold_cfar(i) = threshold;
    % TODO: Measure the signal within the CUT
    signal = X(i + T + G)
    % add signal value to the signal_cfar vector
    signal_cfar(i) = signal;
end

figure(1);
tiledlayout(2,1)
nexttile
plot(signal_cfar)

% plot original sig, threshold and filtered signal within the same figure.
nexttile
plot(X);
hold on
plot(circshift(threshold_cfar,G),'r--','LineWidth',2)
hold on
plot (circshift(signal_cfar,(T+G)),'g--','LineWidth',2);
legend('Signal','CFAR Threshold','detection')