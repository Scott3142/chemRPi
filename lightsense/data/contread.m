function contread
    
%     filename = '19-11-17--1646.csv';
    filename = '19-11-17--1650.csv';
    A = dlmread(filename);
    
    time = A(:,1); voltavg = A(:,2);
    
    timeinterp = 0:0.1:time(end);
    voltinterp = spline(time,voltavg,timeinterp);
    
    grad = zeros(size(timeinterp)); tend = 20;
    for j = 1:length(timeinterp)-tend
        grad(j) = (voltinterp(j+10)-voltinterp(j))/(timeinterp(j+10)-timeinterp(j));
    end
    
    figure(1)
    plot(time,voltavg,'r'); hold on;
    ylim([0 3.5]); xlim([0 6000]);
    x1 = xlabel('time'); y1 = ylabel('V');
    set([x1 y1],'interpreter','latex');
    
    figure(2)
    plot(exp(timeinterp),exp(grad),'g'); hold on;
    xlim([0 40000]);
    x1 = xlabel('time'); y1 = ylabel('dV/dt');
    set([x1 y1],'interpreter','latex');

end