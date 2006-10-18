
%bcond_with unicode

%include	/usr/lib/rpm/macros.perl
Summary:	wxPerl - a Perl wrapper for the wxWidgets C++ GUI toolkit
Summary(pl):	wxPerl - wrapper toolkitu wxWidgets dla Perla
Name:		perl-Wx
Version:    0.27
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Wx/Wx-%{version}.tar.gz
# Source0-md5:	348c65384bbbe48e77f2b57d0a10821e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:  wxGTK2-%{?with_unicode:unicode-}devel >= 2.6.3-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wxPerl - a Perl wrapper for the wxWidgets C++ GUI toolkit

%description -l pl
wxPerl - wrapper toolkitu wxWidgets dla Perla

%prep
%setup -q -n Wx-%{version}

%build
export WX_CONFIG=wx-gtk2-%{?with_unicode:unicode}%{!?with_unicode:ansi}-config
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
    OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/auto/Wx
%dir %{perl_vendorarch}/auto/Wx/Calendar
%dir %{perl_vendorarch}/auto/Wx/DateTime
%dir %{perl_vendorarch}/auto/Wx/DND
%dir %{perl_vendorarch}/auto/Wx/DocView
%dir %{perl_vendorarch}/auto/Wx/FS
%dir %{perl_vendorarch}/auto/Wx/Grid
%dir %{perl_vendorarch}/auto/Wx/Help
%dir %{perl_vendorarch}/auto/Wx/Html
%dir %{perl_vendorarch}/auto/Wx/MDI
%dir %{perl_vendorarch}/auto/Wx/Print
%dir %{perl_vendorarch}/auto/Wx/Socket
%dir %{perl_vendorarch}/auto/Wx/STC
%dir %{perl_vendorarch}/auto/Wx/XRC
%dir %{perl_vendorarch}/auto/Wx/*/*.bs
%{perl_vendorarch}/auto/Wx/*.bs
%{perl_vendorarch}/Wx
%{perl_vendorarch}/Wx.pm
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/*/*.so
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/*.so
%{_mandir}/man3/*
