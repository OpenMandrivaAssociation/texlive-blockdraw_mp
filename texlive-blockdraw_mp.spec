Name:		texlive-blockdraw_mp
Version:	15878
Release:	1
Summary:	Block diagrams and bond graphs, with MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/blockdraw_mp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blockdraw_mp.r15878.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blockdraw_mp.doc.r15878.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of simple MetaPost macros for the task. While the task is
not itself difficult to program, it is felt that many users
will be happy to have a library for the job..

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/blockdraw_mp/blockdraw.mp
%{_texmfdistdir}/metapost/blockdraw_mp/bonddemo.mp
%{_texmfdistdir}/metapost/blockdraw_mp/bondgraph.mp
%{_texmfdistdir}/metapost/blockdraw_mp/cascadedemo.mp
%{_texmfdistdir}/metapost/blockdraw_mp/docblockprefs.mp
%{_texmfdistdir}/metapost/blockdraw_mp/shiftoff.mp
%doc %{_texmfdistdir}/doc/metapost/blockdraw_mp/README
%doc %{_texmfdistdir}/doc/metapost/blockdraw_mp/blockdraw_mp.pdf
%doc %{_texmfdistdir}/doc/metapost/blockdraw_mp/blockdraw_mp.tex
%doc %{_texmfdistdir}/doc/metapost/blockdraw_mp/bonddemo.pdf
%doc %{_texmfdistdir}/doc/metapost/blockdraw_mp/cascadedemo.pdf
%doc %{_texmfdistdir}/doc/metapost/blockdraw_mp/tiddetext.sty
%doc %{_texmfdistdir}/doc/metapost/blockdraw_mp/tighttoc.sty

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
