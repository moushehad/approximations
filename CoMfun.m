function [x,y] = CoMfun(m1,x1,y1,m2,x2,y2,m3,x3,y3)

% this function takes the masses and locations in the cartesian plane
% of three particels *^ 
% and computes and plots their center of mass

% *^ can be easily altered to plot the center mass 
%    of any number of particles


% parametric equations for the center of mass
x = (m1*x1 + m2*x2 + m3*x3) / (m1 + m2 + m3);
y = (m1*y1 + m2*y2 + m3*y3) / (m1 + m2 + m3);

% vectors for plotting the polygon connecting the weights
x_vec = [x1 x2 x3 x1];
y_vec = [y1 y2 y3 y1];

% plot triangle
plot(x_vec, y_vec, 'k-'); 
hold on;

% plot center of mass
plot(x, y, 'bo');

% plot particles
plot([x1 x2 x3], [y1 y2 y3], 'ro');

% add text labels
label1 = sprintf('  m1 = %.1f',m1);
label2 = sprintf('  m2 = %.1f',m2);
label3 = sprintf('  m3 = %.1f',m3);
text(x1, y1, label1);
text(x2, y2, label2);
text(x3, y3, label3);
label = sprintf('  CoM (%.1f, %.1f)', x, y);
text(x, y, label, 'Color', 'b');

% add legend and formatting
legend('Polygon', 'Center of Mass', 'Particles');
title('Particles and Center of Mass');
grid on;
axis equal;

hold off

fprintf('The center of mass is at (%5.1f, %5.1f)\n',x,y)