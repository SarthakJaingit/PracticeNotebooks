Fs = 1000;            % Sampling frequency                    
T = 1/Fs;             % Sampling period       
L = 1500;             % Length of signal
t = (0:L-1)*T;        % Time vector

% Form a signal containing a 50 Hz sinusoid of amplitude 0.7 and a 120 Hz 
% sinusoid of amplitude 1.

S = 0.7 * sin(2 * pi * 50 * t) + sin(2 * pi * 120 * t);
X = S + 2*randn(size(t));

figure(1);
tiledlayout(1,2)

% left plot
nexttile
plot(1000*t(1:50), X(1:50))
title('Signal corrupted with Zero-Mean Random Noise')
xlabel('t (milliseconds)')
ylabel('X(t)')

Y = abs(fft(X)); 
P1 = Y(1:L/2 + 1); 

f = Fs*(0:(L/2))/L;

nexttile
plot(f,P1) 
title('Single-Sided Amplitude Spectrum of X(t)')
xlabel('f (Hz)')
ylabel('|P1(f)|')

% Implement a second FFT along the second dimension to determine the 
% doppler frequency shift.

% First we need to generate a 2D signal
% Convert 1D signal X to 2D using reshape

% while reshaping a 1D signal to 2D we need to ensure that dimensions match
% length(X) = M*N

M = length(X)/50;
N = length(X)/30;

X_2d = reshape(X, [M, N]);

figure(2);
tiledlayout(1,2)

nexttile
imagesc(X_2d)

P1 = fft2(X_2d, M, N)
P1 = abs(fftshift(P1)); 

nexttile 
imagesc(P1)


