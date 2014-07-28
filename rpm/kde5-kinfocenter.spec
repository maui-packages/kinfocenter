# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       kde5-kinfocenter
Summary:    KDE Info Center
Version:    5.0.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kde5-kinfocenter.yaml
Source101:  kde5-kinfocenter-rpmlintrc
Requires:   kde5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  kde5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  kf5-kcompletion-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-solid-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  libX11-devel
BuildRequires:  pciutils-devel
BuildRequires:  libraw1394-devel
BuildRequires:  desktop-file-utils


%description
KDE Info Center




%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kde5_make
# << build pre



# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
%kde5_make_install
# << install pre

# >> install post
# << install post
desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop






%files
%defattr(-,root,root,-)
%doc COPYING COPYING.DOC
%{_kde5_bindir}/kinfocenter
%{_kde5_plugindir}/*.so
%{_kde5_datadir}/kinfocenter
%{_kde5_datadir}/kcmview1394
%{_kde5_datadir}/kcmusb
%{_kde5_sysconfdir}/xdg/menus/kde-information.menu
%{_datadir}/applications/kinfocenter.desktop
%{_datadir}/doc/HTML/en/kinfocenter
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservicetypes5/*.desktop
%{_datadir}/desktop-directories/kde-information.directory
# >> files
# << files


