#!/usr/bin/perl

################################
#  By Chaance                  #
#  Admin Control Panel Finder  #
#    NoobSecToolkit Edition    #
################################

use HTTP::Request;
use LWP::UserAgent;

system('cls');
system('title Admin Control Panel Finder ');

print " Enter the website you want to scan \n";
print" e.g.: www.domain.com or www.domain.com/path\n";
print" --> ";
$site=<STDIN>;
chomp $site;

print "\n\n";
print " Enter the coding language of the website \n";
print" e.g.: asp, php, cfm, any\n";
print" If you don't know the launguage used in the coding then simply type ** any ** \n";
print"--> ";
$code=<STDIN>;
chomp($code);

if ( $site !~ /^http:/ ) {
$site = 'http://' . $site;
}
if ( $site !~ /\/$/ ) {
$site = $site . '/';
}
print "\n";

print "->The website: $site\n";
print "->Source of the website: $code\n";
print "->Scan of the admin control panel is progressing...\n\n\n";

if($code eq "asp"){

@path1=('_admin/','backoffice/','admin/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp',
'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
'administrator/account.asp','administrator.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','pages/admin/admin-login.html','admin/admin-login.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html'
);

foreach $ways(@path1){

$final=$site.$ways;

my $req=HTTP::Request->new(GET=>$final);
my $ua=LWP::UserAgent->new();
$ua->timeout(30);
my $response=$ua->request($req);

if($response->content =~ /Username/ ||
$response->content =~ /Password/ ||
$response->content =~ /username/ ||
$response->content =~ /password/ ||
$response->content =~ /USERNAME/ ||
$response->content =~ /PASSWORD/ ||
$response->content =~ /Senha/ ||
$response->content =~ /senha/ ||
$response->content =~ /Personal/ ||
$response->content =~ /Usuario/ ||
$response->content =~ /Clave/ ||
$response->content =~ /Usager/ ||
$response->content =~ /usager/ ||
$response->content =~ /Sing/ ||
$response->content =~ /passe/ ||
$response->content =~ /P\/W/ ||
$response->content =~ /Admin Password/
){
print " \n [+] Found -> $final\n\n";
print " \n Congratulation, this admin login page is working. \n\n Good luck \n\n";
}else{
print "[-] Not Found <- $final\n";
}
}
}




# -------------------------------------------------------
# -------------------test cfm ---------------------------|
# -------------------------------------------------------





if($code eq "cfm"){

@path1=('_admin/','backoffice/','admin/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','account.cfm','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm',
'admin_area/admin.cfm','admin_area/login.cfm','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
'admin/home.cfm','admin/controlpanel.cfm','admin.cfm','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm','admin/cp.cfm','cp.cfm',
'administrator/account.cfm','administrator.cfm','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm','administrator/login.cfm',
'moderator/admin.cfm','controlpanel.cfm','admin/account.html','adminpanel.html','webadmin.html','pages/admin/admin-login.html','admin/admin-login.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.cfm','user.html','admincp/index.cfm','admincp/login.cfm','admincp/index.html',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
'admincontrol/login.html','adm/index.html','adm.html','admincontrol.cfm','admin/account.cfm','adminpanel.cfm','webadmin.cfm','webadmin/index.cfm',
'webadmin/admin.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm','panel-administracion/login.cfm','adminLogin.cfm',
'admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm','adminarea/admin.cfm','adminarea/login.cfm','admin-login.html',
'panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm','modelsearch/admin.cfm','administrator/index.cfm',
'admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','adm/index.cfm',
'adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html'
);

foreach $ways(@path1){

$final=$site.$ways;

my $req=HTTP::Request->new(GET=>$final);
my $ua=LWP::UserAgent->new();
$ua->timeout(30);
my $response=$ua->request($req);

if($response->content =~ /Username/ ||
$response->content =~ /Password/ ||
$response->content =~ /username/ ||
$response->content =~ /password/ ||
$response->content =~ /USERNAME/ ||
$response->content =~ /PASSWORD/ ||
$response->content =~ /Senha/ ||
$response->content =~ /senha/ ||
$response->content =~ /Personal/ ||
$response->content =~ /Usuario/ ||
$response->content =~ /Clave/ ||
$response->content =~ /Usager/ ||
$response->content =~ /usager/ ||
$response->content =~ /Sing/ ||
$response->content =~ /passe/ ||
$response->content =~ /P\/W/ ||
$response->content =~ /Admin Password/
){
print " \n [+] Found -> $final\n\n";
print " \n Congratulation, this admin login page is working. \n\n Good luck \n\n";
}else{
print "[-] Not Found <- $final\n";
}
}
}





# -------------------------------------------------------
#--------------------------/test-------------------------|
# -------------------------------------------------------


if($code eq "php"){

@path2=('_admin/','backoffice/','admin/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php'
);

foreach $ways(@path2){

$final=$site.$ways;

my $req=HTTP::Request->new(GET=>$final);
my $ua=LWP::UserAgent->new();
$ua->timeout(30);
my $response=$ua->request($req);

if($response->content =~ /Username/ ||
$response->content =~ /Password/ ||
$response->content =~ /username/ ||
$response->content =~ /password/ ||
$response->content =~ /USERNAME/ ||
$response->content =~ /PASSWORD/ ||
$response->content =~ /Senha/ ||
$response->content =~ /senha/ ||
$response->content =~ /Personal/ ||
$response->content =~ /Usuario/ ||
$response->content =~ /Clave/ ||
$response->content =~ /Usager/ ||
$response->content =~ /usager/ ||
$response->content =~ /Sing/ ||
$response->content =~ /passe/ ||
$response->content =~ /P\/W/ ||
$response->content =~ /Admin Password/
){
print " \n [+] Found -> $final\n\n";
print " \n Congratulation, this admin login page is working. \n\n Good luck \n\n";
}else{
print "[-] Not Found <- $final\n";
}
}
}




# -------------------------------------------------------
# ----------------------- any ---------------------------|
# -------------------------------------------------------





if($code eq "any"){

@path1=('_admin/','backoffice/','account.asp','account.cfm','account.html','account.php','acct_login/','adm.asp','adm.cfm','adm.html','adm.php','adm/','adm/admloginuser.asp','adm/admloginuser.cfm','adm/admloginuser.php','adm/index.asp','adm/index.cfm','adm/index.html','adm/index.php','adm_auth.asp','adm_auth.cfm','adm_auth.php','admin.asp','admin.cfm','admin.html','admin.php','admin/','admin/account.asp','admin/account.cfm','admin/account.html','admin/account.php','admin/admin.asp','admin/admin.cfm','admin/admin.html','admin/admin.php','admin/admin_login.asp','admin/admin_login.cfm','admin/admin_login.html','admin/admin_login.php','admin/adminLogin.asp','admin/admin-login.asp','admin/adminLogin.cfm','admin/admin-login.cfm','admin/adminLogin.html','admin/admin-login.html','admin/adminLogin.php','admin/admin-login.php','admin/controlpanel.asp','admin/controlpanel.cfm','admin/controlpanel.html','admin/controlpanel.php','admin/cp.asp','admin/cp.cfm','admin/cp.html','admin/cp.php','admin/home.asp','admin/home.cfm','admin/home.html','admin/home.php','admin/index.asp','admin/index.cfm','admin/index.html','admin/index.php','admin/login.asp','admin/login.cfm','admin/login.html','admin/login.php','admin_area/','admin_area/admin.asp','admin_area/admin.cfm','admin_area/admin.html','admin_area/admin.php','admin_area/index.asp','admin_area/index.cfm','admin_area/index.html','admin_area/index.php','admin_area/login.asp','admin_area/login.cfm','admin_area/login.html','admin_area/login.php','admin_login.asp','admin_login.cfm','admin_login.html','admin_login.php','admin1.asp','admin1.html','admin1.php','admin1/','admin2.asp','admin2.cfm','admin2.html','admin2.php','admin2/index.asp','admin2/index.cfm','admin2/index.php','admin2/login.asp','admin2/login.cfm','admin2/login.php','admin4_account/','admin4_colon/','adminarea/','adminarea/admin.asp','adminarea/admin.cfm','adminarea/admin.html','adminarea/admin.php','adminarea/index.asp','adminarea/index.cfm','adminarea/index.html','adminarea/index.php','adminarea/login.asp','adminarea/login.cfm','adminarea/login.html','adminarea/login.php','admincontrol.asp','admincontrol.cfm','admincontrol.html','admincontrol.php','admincontrol/login.asp','admincontrol/login.cfm','admincontrol/login.html','admincontrol/login.php','admincp/index.asp','admincp/index.cfm','admincp/index.html','admincp/login.asp','admincp/login.cfm','administer/','administr8.asp','administr8.html','administr8.php','administr8/','administratie/','administration.html','administration.php','administration/','administrator.asp','administrator.cfm','administrator.html','administrator.php','administrator/','administrator/account.asp','administrator/account.cfm','administrator/account.html','administrator/account.php','administrator/index.asp','administrator/index.cfm','administrator/index.html','administrator/index.php','administrator/login.asp','administrator/login.cfm','administrator/login.html','administrator/login.php','administratoraccounts/','administratorlogin.asp','administratorlogin.cfm','administratorlogin.php','administratorlogin/','administrators/','administrivia/','adminLogin.asp','admin-login.asp','adminLogin.cfm','admin-login.cfm','adminLogin.html','admin-login.html','adminLogin.php','admin-login.php','adminLogin/','adminpanel.asp','adminpanel.cfm','adminpanel.html','adminpanel.php','adminpro/','admins.asp','admins.html','admins.php','admins/','AdminTools/','admloginuser.asp','admloginuser.cfm','admloginuser.php','affiliate.asp','affiliate.cfm','affiliate.php','autologin/','banneradmin/','bbadmin/','bb-admin/','bb-admin/admin.asp','bb-admin/admin.cfm','bb-admin/admin.html','bb-admin/admin.php','bb-admin/index.asp','bb-admin/index.cfm','bb-admin/index.html','bb-admin/index.php','bb-admin/login.asp','bb-admin/login.cfm','bb-admin/login.html','bb-admin/login.php','bigadmin/','blogindex/','cadmins/','ccp14admin/','cmsadmin/','controlpanel.asp','controlpanel.cfm','controlpanel.html','controlpanel.php','controlpanel/','cp.asp','cp.cfm','cp.html','cp.php','cPanel/','cpanel_file/','customer_login/','database_administration/','directadmin/','dir-login/','ezsqliteadmin/','fileadmin.asp','fileadmin.html','fileadmin.php','fileadmin/','formslogin/','globes_admin/','home.asp','home.cfm','home.html','home.php','hpwebjetadmin/','Indy_admin/','instadmin/','irc-macadmin/','LiveUser_Admin/','login.asp','login.cfm','login.html','login.php','login_db/','login1/','loginflat/','login-redirect/','login-us/','logo_sysadmin/','Lotus_Domino_Admin/','macadmin/','manuallogin/','memberadmin.asp','memberadmin.cfm','memberadmin.php','memberadmin/','members/','memlogin/','meta_login/','modelsearch/admin.asp','modelsearch/admin.cfm','modelsearch/admin.html','modelsearch/admin.php','modelsearch/index.asp','modelsearch/index.cfm','modelsearch/index.html','modelsearch/index.php','modelsearch/login.asp','modelsearch/login.cfm','modelsearch/login.html','modelsearch/login.php','moderator.asp','moderator.cfm','moderator.html','moderator.php','moderator/','moderator/admin.asp','moderator/admin.cfm','moderator/admin.html','moderator/admin.php','moderator/login.asp','moderator/login.cfm','moderator/login.html','moderator/login.php','myadmin/','navSiteAdmin/','newsadmin/','nsw/admin/login.php','openvpnadmin/','pages/admin/admin-login.asp','pages/admin/admin-login.cfm','pages/admin/admin-login.html','pages/admin/admin-login.php','panel/','panel-administracion/','panel-administracion/admin.asp','panel-administracion/admin.cfm','panel-administracion/admin.html','panel-administracion/admin.php','panel-administracion/index.asp','panel-administracion/index.cfm','panel-administracion/index.html','panel-administracion/index.php','panel-administracion/login.asp','panel-administracion/login.cfm','panel-administracion/login.html','panel-administracion/login.php','pgadmin/','phpldapadmin/','phpmyadmin/','phppgadmin/','phpSQLiteAdmin/','platz_login/','power_user/','project-admins/','pureadmin/','radmind/','radmind-1/','rcjakar/admin/login.php','rcLogin/','Server.asp','Server.html','Server.php','server/','server_admin_small/','ServerAdministrator/','showlogin/','simpleLogin/','siteadmin/index.asp','siteadmin/index.cfm','siteadmin/index.php','siteadmin/login.asp','siteadmin/login.cfm','siteadmin/login.html','siteadmin/login.php','smblogin/','sql-admin/','ss_vms_admin_sm/','sshadmin/','staradmin/','sub-login/','Super-Admin/','support_login/','sysadmin.asp','sysadmin.html','sysadmin.php','sysadmin/','sys-admin/','SysAdmin2/','sysadmins/','system_administration/','system-administration/','typo3/','ur-admin.asp','ur-admin.html','ur-admin.php','ur-admin/','user.asp','user.html','user.php','useradmin/','UserLogin/','utility_login/','vadmind/','vmailadmin/','webadmin.asp','webadmin.cfm','webadmin.html','webadmin.php','WebAdmin/','webadmin/admin.asp','webadmin/admin.cfm','webadmin/admin.html','webadmin/admin.php','webadmin/index.asp','webadmin/index.cfm','webadmin/index.html','webadmin/index.php','webadmin/login.asp','webadmin/login.cfm','webadmin/login.html','webadmin/login.php','wizmysqladmin/','wp-admin/','wp-login.php','wp-login/','xlogin/','yonetici.asp','yonetici.html','yonetici.php','yonetim.asp','yonetim.html','yonetim.php','panel/?a=cp'
);

foreach $ways(@path1){

$final=$site.$ways;

my $req=HTTP::Request->new(GET=>$final);
my $ua=LWP::UserAgent->new();
$ua->timeout(30);
my $response=$ua->request($req);

if($response->content =~ /Username/ ||
$response->content =~ /Password/ ||
$response->content =~ /username/ ||
$response->content =~ /password/ ||
$response->content =~ /USERNAME/ ||
$response->content =~ /PASSWORD/ ||
$response->content =~ /Senha/ ||
$response->content =~ /senha/ ||
$response->content =~ /Personal/ ||
$response->content =~ /Usuario/ ||
$response->content =~ /Clave/ ||
$response->content =~ /Usager/ ||
$response->content =~ /usager/ ||
$response->content =~ /Sing/ ||
$response->content =~ /passe/ ||
$response->content =~ /P\/W/ ||
$response->content =~ /Admin Password/
){
print " \n [+] Found -> $final\n\n";
print " \n Congratulation, this admin login page is working. \n\n Good luck from Chaance \n\n";
}else{
print "[-] Not Found <- $final\n";
}
}
kill("STOP",NULL);
}

##
