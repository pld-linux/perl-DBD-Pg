#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_with	dbtests	# tests using local PostgreSQL installation
#
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
Version:	3.20.2
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/DBD/TURNSTEP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	47df9e208d26be363332bcdde538a859
URL:		https://metacpan.org/dist/DBD-Pg
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.58
BuildRequires:	perl-DBI >= 1.614
BuildRequires:	perl-devel >= 1:5.8.1
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-Time-HiRes
BuildRequires:	perl-version
%endif
BuildRequires:	postgresql-devel >= 8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.749
Requires:	perl-DBI >= 1.614
# version not detected
Provides:	perl(DBD::Pg) = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
export POSTGRES_LIB="%{_libdir}"
export POSTGRES_INCLUDE="%{_includedir}/postgresql"
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags} -std=gnu17"

# skip SIGNATURE test (uses network to get PGP key)
%{__rm} SIGNATURE
%if %{with tests}
%{__make} test \
	%{!?with_dbtests:DBI_DSN=NOWAY}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# remove "tool" to install Perl modules
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Bundle/DBD/Pg.pm \
	$RPM_BUILD_ROOT%{_mandir}/man3/Bundle::DBD::Pg.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/DBD/Pg.pm
%dir %{perl_vendorarch}/auto/DBD/Pg
%{perl_vendorarch}/auto/DBD/Pg/Pg.so
%{_mandir}/man3/DBD::Pg.3pm*
