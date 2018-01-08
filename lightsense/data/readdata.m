function readdata(mlreq)

%     filename = 'example.csv';
    filename = '19-11-17--1530.csv';
    A = dlmread(filename);
    
    mlvol = A(:,1); voltavg = A(:,2);
    
    mlinterp = 0:0.1:5;
    vinterp = spline(mlvol,voltavg);
    
    vreq = ppval(vinterp,mlreq);
    disp(['Reading at prescribed ml level: ' num2str(vreq) 'V']);
    
    plot(mlvol,voltavg,'ko','markerfacecolor','r'); hold on;
    plot(mlinterp,ppval(vinterp,mlinterp),'-b','linewidth',2); 
    plot(mlreq,vreq,'ko','markerfacecolor','g');
    line([mlreq mlreq],[0 vreq],'color','g','linestyle','--','linewidth',2);
    line([0 mlreq],[vreq vreq],'color','g','linestyle','--','linewidth',2); hold off;
    xlim([0 5]); ylim([0 3.5]);
    x1 = xlabel('ml'); y1 = ylabel('V');
    set([x1 y1],'interpreter','latex');

end