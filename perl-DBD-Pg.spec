#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
%bcond_with	dbtests	# perform tests using local PostgreSQL installation
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBD
%define		pnam	Pg
Summary:	A PostgresSQL interface for Perl
Summary(cs.UTF-8):	PostgresSQL rozhraní pro Perl
Summary(da.UTF-8):	Et PostgreSQL-grænseflade for Perl
Summary(de.UTF-8):	Ein PostgreSQL-Interface für Perl
Summary(es.UTF-8):	Interfaz PostgresSQL para Perl
Summary(fr.UTF-8):	Interface PostgresSQL pour Perl
Summary(it.UTF-8):	Interfaccia PostgreSQL per Perl
Summary(ja.UTF-8):	Perl の PostgreSQL インターフェイス
Summary(ko.UTF-8):	펄을 위한 PostgresSQL 인터페이스
Summary(nb.UTF-8):	Et PostgreSQL-grensesnitt for Perl
Summary(pl.UTF-8):	Perlowy interfejs do PostgresSQL-a
Summary(pt.UTF-8):	Uma interface de Perl para o PostgresSQL
Summary(pt_BR.UTF-8):	Uma interface de Perl para o PostgresSQL
Summary(ru.UTF-8):	Интерфейс PostgresSQL для Perl
Summary(sv.UTF-8):	Ett gränssnitt till PostgresSQL för Perl
Summary(uk.UTF-8):	Perl-інтерфейс до PostgresSQL
Summary(zh_CN.UTF-8):	Perl 的 PostgresSQL 界面。
Name:		perl-DBD-Pg
Version:	2.19.3
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/T/TU/TURNSTEP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	026ea19f89aee12051bce23d797e824b
URL:		http://search.cpan.org/dist/DBD-Pg/
BuildRequires:	perl-DBI
BuildRequires:	perl-devel >= 1:5.8.0
%{?with_tests:BuildRequires:	perl-version}
BuildRequires:	postgresql-devel
BuildRequires:	rpm-perlprov >= 4.1-13
Provides:	perl(DBD::Pg) = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq 'perl(POSIX(qw(isprint)))'

%description
DBD::Pg - PostgreSQL database driver for the DBI module.

%description -l cs.UTF-8
Implementace DBI pro PostgreSQL do Perlu.

%description -l da.UTF-8
Denne pakke indeholder en implementation af DBI for PostgreSQL for
Perl.

%description -l de.UTF-8
Dieses Paket enthält eine Implementierung von PostgreSQL für Perl.

%description -l es.UTF-8
Este paquete contiene una implementación de DBI para PotgreSQL para
PERL.

%description -l fr.UTF-8
Ce paquetage contient une mise en oeuvre de DBI pour PostgreSQL pour
Perl.

%description -l it.UTF-8
Questo pacchetto contiene un'implementazione di DBI per PostgreSQL per
Perl.

%description -l ja.UTF-8
このパッケージには Perl の PostgreSQL 用 DBI 実装が収録されています。

%description -l ko.UTF-8
이 패키지는 펄을 위한 PostgreSQL의 DBI 실현을 포함하고 있습니다.

%description -l nb.UTF-8
Denne pakken inneholder en implementasjon av DBI for PostgreSQL for
Perl.

%description -l pl.UTF-8
DBD::Pg - Sterownik bazy danych PostgreSQL dla modułu DBI.

%description -l pt.UTF-8
Este pacote contém uma implementação de DBI para o PostgreSQL para o
Perl.

%description -l pt_BR.UTF-8
Este pacote contém uma implementação de DBI para o PostgreSQL para o
Perl.

%description -l ru.UTF-8
Это пакет содержит реализацию DBI для PostgreSQL для Perl.

%description -l sv.UTF-8
Detta paket innehåller en implementation av DBI för PostgreSQL för
Perl.

%description -l zh_CN.UTF-8
该软件包包括用于 Perl 的 PostgreSQL 的 DBI 实现。

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
POSTGRES_LIB="%{_libdir}"; export POSTGRES_LIB
POSTGRES_INCLUDE="%{_includedir}/postgresql"; export POSTGRES_INCLUDE
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

# skip SIGNATURE test (uses network to get PGP key)
rm SIGNATURE
%{?with_tests:%{__make} test %{!?with_dbtests:DBI_DSN=NOWAY}}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/DBD/Pg.pm
%dir %{perl_vendorarch}/auto/DBD/Pg
%attr(755,root,root) %{perl_vendorarch}/auto/DBD/Pg/Pg.so
%{_mandir}/man3/*
