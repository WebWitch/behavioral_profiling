opts = detectImportOptions('Documents/logs/log_LAPS_CAN_2019_05_15_20_08_16.csv');
opts.SelectedVariableNames = [2 8 4];
m = readtable('Documents/logs/log_LAPS_CAN_2019_05_15_20_08_16.csv',opts);
x1=m{:,1};
y1=m{:,2};
x12=m{:,3};
ax1 = subplot(4,1,1);
plot(ax1,x1,y1,'Color','blue');
title(ax1,'Speed VS Time - Lap 1');
ylabel(ax1,'Speed (km/h)');
xlabel(ax1,'Timestamp');
opts = detectImportOptions('Documents/logs/log_LAPS_CAN_2019_05_15_20_31_29.csv');
opts.SelectedVariableNames = [2 8 4];
m = readtable('Documents/logs/log_LAPS_CAN_2019_05_15_20_31_29.csv',opts);
x2=m{:,1};
y2=m{:,2};
x22=m{:,3};
ax2 = subplot(4,1,2);
plot(ax2,x2,y2,'Color','red');
title(ax2,'Speed VS Time - Lap 2');
ylabel(ax2,'Speed (km/h)');
xlabel(ax2,'Timestamp');
opts = detectImportOptions('Documents/logs/log_LAPS_CAN_2019_05_15_20_51_43.csv');
opts.SelectedVariableNames = [2 8 4];
m = readtable('Documents/logs/log_LAPS_CAN_2019_05_15_20_51_43.csv',opts);
x3=m{:,1};
y3=m{:,2};
x32=m{:,3};
ax3 = subplot(4,1,3);
plot(ax3,x3,y3,'Color','black');
title(ax3,'Speed VS Time - Lap 3');
ylabel(ax3,'Speed (km/h)');
xlabel(ax3,'Timestamp');
ax4 = subplot(4,1,4);
hold(ax4,'on');
plot(ax4,x12,y1,'Color','blue');
plot(ax4,x22,y2,'Color','red');
plot(ax4,x32,y3,'Color','black');
hold(ax4,'off');
title(ax4,'Speed VS Time - Lap 1 vs 2 vs 3');
ylabel(ax4,'Speed (km/h)');
xlabel(ax4,'Time (s)');