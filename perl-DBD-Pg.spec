%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	Pg
Summary:	A PostgresSQL interface for Perl
Summary(cs):	PostgresSQL rozhran� pro Perl
Summary(da):	Et PostgreSQL-gr�nseflade for Perl
Summary(de):	Ein PostgreSQL-Interface f�r Perl
Summary(es):	Interfaz PostgresSQL para Perl
Summary(fr):	Interface PostgresSQL pour Perl
Summary(it):	Interfaccia PostgreSQL per Perl
Summary(ja):	Perl �� PostgreSQL ���󥿡��ե�����
Summary(ko):	���� ���� PostgresSQL �������̽�
Summary(no):	Et PostgreSQL-grensesnitt for Perl
Summary(pl):	Modu� perla DBD::Pg
Summary(pt):	Uma interface de Perl para o PostgresSQL
Summary(ru):	��������� PostgresSQL ��� Perl
Summary(sv):	Ett gr�nssnitt till PostgresSQL f�r Perl
Summary(uk):	Perl-��������� �� PostgresSQL
Summary(zh_CN):	Perl �� PostgresSQL ���档
Name:		perl-DBD-Pg
Version:	1.21
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-DBI
BuildRequires:	postgresql-devel
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq "perl(POSIX(qw(isprint)))"

%description
DBD::Pg - PostgreSQL database driver for the DBI module.

%description -l cs
Implementace DBI pro PostgreSQL do Perlu.

%description -l da
Denne pakke indeholder en implementation af DBI for PostgreSQL for
Perl.

%description -l de
Dieses Paket enth�lt eine Implementierung von PostgreSQL f�r Perl.

%description -l es
Este paquete contiene una implementaci�n de DBI para PotgreSQL para
PERL.

%description -l fr
Ce paquetage contient une mise en oeuvre de DBI pour PostgreSQL pour
Perl.

%description -l it
Questo pacchetto contiene un'implementazione di DBI per PostgreSQL per
Perl.

%description -l ja
���Υѥå������ˤ� Perl �� PostgreSQL �� DBI ��������Ͽ����Ƥ��ޤ���

%description -l ko
�� ��Ű���� ���� ���� PostgreSQL�� DBI ������ �����ϰ� �ֽ��ϴ�.

%description -l no
Denne pakken inneholder en implementasjon av DBI for PostgreSQL for
Perl.

%description -l pl
DBD::Pg - Sterownik bazy danych PostgreSQL dla modu�u DBI.

%description -l pt
Este pacote cont�m uma implementa��o de DBI para o PostgreSQL para o
Perl.

%description -l ru
��� ����� �������� ���������� DBI ��� PostgreSQL ��� Perl.

%description -l sv
Detta paket inneh�ller en implementation av DBI f�r PostgreSQL f�r
Perl.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
POSTGRES_LIB="%{_libdir}"; export POSTGRES_LIB
POSTGRES_INCLUDE="%{_includedir}/postgresql"; export POSTGRES_INCLUDE
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/DBD/*
%dir %{perl_vendorarch}/auto/DBD/Pg
%{perl_vendorarch}/auto/DBD/Pg/Pg.bs
%attr(755,root,root) %{perl_vendorarch}/auto/DBD/Pg/Pg.so
%{_mandir}/man[13]/*
