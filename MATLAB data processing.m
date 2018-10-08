for i =1:65
    filename{i}=sprintf('4_19_%s.txt',num2str(i));
    h{i}=[5 5];
    h2{i}=fspecial('average',[5 5]);
end
%%
Tdata=cellfun(@load,filename,'Uniformoutput',false);
%%
Tfilt=cellfun(@(x)x(5:end-5,5:end-5),cellfun(@medfilt2,Tdata,h,'Uniformoutput',false),'Uniformoutput',false);
%%
Tavg=cellfun(@(x)x(5:end-5,5:end-5),cellfun(@imfilter,Tdata,h2,'Uniformoutput',false),'Uniformoutput',false);
%Tavg=cellfun(@(x)x(5:end-5,5:end-5),Tdata,'Uniformoutput',false);

%%
%%
%begin fitting
yy=(1:151)';
%yy=(1:310)';
%yy=num2cell(repmat(yy,1,111*i),1);
%yy=num2cell(repmat(yy,1,230*i),1);
Ta=cellfun(@(x)(x(:,[1:end])),Tavg,'Uniformoutput',false);
cc=num2cell(cell2mat(Ta),1);
[dd,gof]=cellfun(@(x)(createFit(yy,x)), cc,'Uniformoutput',false);
%%
dnew=cellfun(@(x)(feval(x,yy)),dd,'Uniformoutput',false);
%%
%begin fitting
 xx=1:111;
 %xx=1:230;
 
 xx=num2cell(repmat(xx,151*i,1),2);
 %xx=num2cell(repmat(xx,310*i,1),2);
[ee,gof2]=cellfun(@createFit, xx,num2cell(cell2mat(Tavg'),2),'Uniformoutput',false);
%%
enew=cellfun(@feval,ee,xx,'Uniformoutput',false);
%%
%load('res.mat')
%load('enew.mat')
%load('dnew.mat')
%load('Tavg.mat')
%%
 mm=cell2mat(dnew);
nn=cell2mat(enew');
mmm=permute(reshape(mm,151,111,i),[2 1 3]);
 nnn=reshape(nn,111,151,i);
% TTinst=reshape(cell2mat(cellfun(@(x)x(5:end-5,5:end-5),Tdata,'Uniformoutput',false)')',111,151,i);
%%
TTinst=reshape(cell2mat(Tavg')',111,151,i);
 %%
 %res=sum(nnn,3)+sum(mmm,3)-2*sum(TTinst,3);
 res_n=nnn+mmm-2*TTinst;
%%
for i =1:65
   res_nn{i}=res_n(:,:,i);
    hh{i}='sobel';
end
%%
aa3=cellfun(@reshape,cellfun(@edge,res_nn,hh,'Uniformoutput',false),num2cell(111*151*ones(i,1))',num2cell(ones(i,1))',...
    'Uniformoutput',false);
%%
aa4=reshape(cell2mat(aa3),111,151,i);
aan=(sum(aa4,3)).*sum(res_n,3);
%%
Ia=reshape(aan,111*151,1);
opts = statset('Display','final');
[idx,C] = kmeans(Ia,4,'Distance','sqeuclidean',...
'Replicates',18,'Options',opts);
ba=zeros(111*151,1);
 IC=find(C==min(C));
 ba(idx==IC)=1;
ba2=reshape(ba,111,151);

