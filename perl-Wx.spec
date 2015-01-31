#
# Conditional build:
%bcond_without	unicode	# ANSI instead of Unicode version of wxGTK
%bcond_with	gtk3	# wxGTK3 instead of wxGTK2
%bcond_with	tests	# "make test" (requires $DISPLAY)
#
%define		wxpkg	wxGTK%{?with_gtk3:3}%{!?with_gtk3:2}%{?with_unicode:-unicode}
%define		wx_ver		%(rpm -q wxWidgets-devel --qf '%%{VERSION}')
%define		wx_ver_tag	%(echo %{wx_ver} | tr . _)
%define		alien_wxcfg	gtk%{!?with_gtk3:2}_%{wx_ver_tag}%{?with_unicode:_uni}_gcc_3_4
%include	/usr/lib/rpm/macros.perl
Summary:	wxPerl - a Perl wrapper for the wxWidgets C++ GUI toolkit
Summary(pl.UTF-8):	wxPerl - wrapper toolkitu graficznego C++ wxWidgets dla Perla
Name:		perl-Wx
Version:	0.9923
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Wx/Wx-%{version}.tar.gz
# Source0-md5:	16f203d0e3bf9ecc7f830f10bf165c5e
URL:		http://wxperl.sourceforge.net/
BuildRequires:	perl-Alien-wxWidgets >= 0.25
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.46
BuildRequires:	perl-ExtUtils-ParseXS >= 3.15
BuildRequires:	perl-ExtUtils-XSpp >= 0.16_02
%if %{with tests}
BuildRequires:	perl-Test-Harness >= 2.26
BuildRequires:	perl-Test-Simple >= 0.45
%endif
BuildRequires:	perl-devel >= 1:5.8.0
# require Alien::wxWidgets with config for desired wx variant
BuildRequires:	perl(Alien::wxWidgets::Config::%{alien_wxcfg})
BuildRequires:	perl(File::Spec::Functions) >= 0.82
BuildRequires:	perl(if) >= 0.03
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	%{wxpkg}-devel >= 2.6.3-1
Requires:	perl-Alien-wxWidgets >= 0.25
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_perl		Wx::PlValidator

%description
wxPerl is a Perl wrapper for the wxWidgets C++ GUI toolkit.

%description -l pl.UTF-8
wxPerl to wrapper toolkitu graficznego C++ wxWidgets dla Perla.

%package devel
Summary:	Development package for wxPerl
Summary(pl.UTF-8):	Pakiet do rozwijania oprogramowania przy użyciu wxPerla
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{wxpkg}-devel >= 2.6.3-1

%description devel
Development package for wxPerl.

%description devel -l pl.UTF-8
Pakiet do rozwijania oprogramowania przy użyciu wxPerla.

%prep
%setup -q -n Wx-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	--wx-toolkit=gtk%{!?with_gtk3:2} \
	--%{!?with_unicode:no-}wx-unicode
%{__make} \
	CC="%{__cxx}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Wx/*.pod

# not this OS
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Wx/build/MakeMaker/{MacOSX,Win32}* \
	$RPM_BUILD_ROOT%{_mandir}/man3/Wx::build::MakeMaker::Win32_MSVC.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt docs/todo.txt
%{perl_vendorarch}/Wx.pm
%dir %{perl_vendorarch}/Wx
%{perl_vendorarch}/Wx/Perl
%{perl_vendorarch}/Wx/*.pm
%{perl_vendorarch}/Wx/typemap
%dir %{perl_vendorarch}/auto/Wx
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/Wx.so
%dir %{perl_vendorarch}/auto/Wx/AUI
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/AUI/AUI.so
%dir %{perl_vendorarch}/auto/Wx/Calendar
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/Calendar/Calendar.so
%dir %{perl_vendorarch}/auto/Wx/DND
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/DND/DND.so
%dir %{perl_vendorarch}/auto/Wx/DataView
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/DataView/DataView.so
%dir %{perl_vendorarch}/auto/Wx/DateTime
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/DateTime/DateTime.so
%dir %{perl_vendorarch}/auto/Wx/DocView
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/DocView/DocView.so
%dir %{perl_vendorarch}/auto/Wx/FS
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/FS/FS.so
%dir %{perl_vendorarch}/auto/Wx/Grid
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/Grid/Grid.so
%dir %{perl_vendorarch}/auto/Wx/Help
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/Help/Help.so
%dir %{perl_vendorarch}/auto/Wx/Html
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/Html/Html.so
%dir %{perl_vendorarch}/auto/Wx/IPC
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/IPC/IPC.so
%dir %{perl_vendorarch}/auto/Wx/MDI
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/MDI/MDI.so
%dir %{perl_vendorarch}/auto/Wx/Media
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/Media/Media.so
%dir %{perl_vendorarch}/auto/Wx/PerlTest
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/PerlTest/PerlTest.so
%dir %{perl_vendorarch}/auto/Wx/Print
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/Print/Print.so
%dir %{perl_vendorarch}/auto/Wx/PropertyGrid
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/PropertyGrid/PropertyGrid.so
%dir %{perl_vendorarch}/auto/Wx/Ribbon
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/Ribbon/Ribbon.so
%dir %{perl_vendorarch}/auto/Wx/RichText
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/RichText/RichText.so
%dir %{perl_vendorarch}/auto/Wx/STC
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/STC/STC.so
%dir %{perl_vendorarch}/auto/Wx/Socket
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/Socket/Socket.so
%dir %{perl_vendorarch}/auto/Wx/WebView
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/WebView/WebView.so
%dir %{perl_vendorarch}/auto/Wx/XRC
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/XRC/XRC.so
%{_mandir}/man3/Wx.3pm*
%{_mandir}/man3/Wx::Api.3pm*
%{_mandir}/man3/Wx::Loader.3pm*
%{_mandir}/man3/Wx::NewClass.3pm*
%{_mandir}/man3/Wx::Perl::*.3pm*
%{_mandir}/man3/Wx::Socket.3pm*
%{_mandir}/man3/Wx::Thread.3pm*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wxperl_overload
%{perl_vendorarch}/Wx/Overload
%{perl_vendorarch}/Wx/XSP
%{perl_vendorarch}/Wx/build
%{perl_vendorarch}/Wx/cpp
%{_mandir}/man1/wxperl_overload.1p*
%{_mandir}/man3/Wx::XSP::*.3pm*
%{_mandir}/man3/Wx::build::*.3pm*
