clear
clc

% this is a script that allows you to plot a sequence of partial sums.

% right now, it is plotting the alternating sum of
% four times the inverse of each odd number.
% surprisingly, the infinite sum is s = pi. 

% to plot the sequenc of partial sums
% state the last term for approximating infinity
% make a row vector x for plotting against s_n 
% prep s_n for its entries
% first value in s_n: 4 * (-1)^(1-1) / 2(1) - 1 = 4
% starts a loop for the rest of the entries
% each entry is the sum of the last and the current
% end the loop
% the approximation of s is th elast term in s_n

% to plot the sequenc of partial sums
last = 1e2; % state the last term for approximating infinity
x = 1:last; % make a row vector x for plotting against s_n 
s_n = x; % preps s_n for its entries
s_n(1) = 4; % first value in s_n: 4 * (-1)^(1-1) / 2(1) - 1 = 4
for n = 2:last; % starts a loop for the rest of the entries
    s_n(n) = s_n(n-1) + 4*(-1)^(n-1) / (2*n - 1); % each entry is the sum of the last and the current
end % end the loop
s = s_n(end); % the approximation of s is th elast term in s_n

fprintf('The sum s is approximately %4.2f \n',s)
plot(x,s_n)
xlabel('n')
ylabel('s_{n}')
title('Sequence of partial sums s_{n} for 4*(-1)^{n-1}/(2n-1)')
grid on