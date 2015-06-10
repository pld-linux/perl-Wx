
# NOTE: On every new version, we need to manually regenerate the list of XS Provides
# cd Wx-*
# for i in `grep -r "PACKAGE=" * | cut -d " " -f 2 | sed 's|PACKAGE=|perl(|g' | grep "Wx::" | sort -n |uniq`; do printf "Provides: $i)\\n"; done &> provides.txt
# grep -orP '%name{Wx::[^}]*}\s+class' |grep -v "3pm" | cut -d : -f 2- | sed 's|%name{|Provides: perl(|g' | sed 's|} class|)|g' |uniq &>> provides.txt
# cat provides.txt | uniq | sort -n

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
Version:	0.9927
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Wx/Wx-%{version}.tar.gz
# Source0-md5:	ef05f2f1fc0c3ccb1d4d1aa3896196f9
URL:		http://wxperl.sourceforge.net/
BuildRequires:	perl-Alien-wxWidgets >= 0.67
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.46
BuildRequires:	perl-ExtUtils-ParseXS >= 3.15
BuildRequires:	perl-ExtUtils-XSpp >= 0.16_02
%if %{with tests}
BuildRequires:	perl-Test-Harness >= 2.26
BuildRequires:	perl-Test-Simple >= 0.45
%endif
BuildRequires:	perl-devel >= 1:5.8.0
# require Alien::wxWidgets with config for desired wx variant
BuildRequires:	%{wxpkg}-devel >= 2.6.3-1
BuildRequires:	perl(Alien::wxWidgets::Config::%{alien_wxcfg})
BuildRequires:	perl(File::Spec::Functions) >= 0.82
BuildRequires:	perl(if) >= 0.03
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Alien-wxWidgets >= 0.25

# manually generated, see note on top of spec file
Provides:	perl(Wx::ANIHandler)
Provides:	perl(Wx::AUI)
Provides:	perl(Wx::AboutDialogInfo)
Provides:	perl(Wx::AcceleratorEntry)
Provides:	perl(Wx::AcceleratorTable)
Provides:	perl(Wx::ActivateEvent)
Provides:	perl(Wx::Animation)
Provides:	perl(Wx::AnimationCtrl)
Provides:	perl(Wx::App)
Provides:	perl(Wx::ArchiveFSHandler)
Provides:	perl(Wx::ArrayStringProperty)
Provides:	perl(Wx::ArtProvider)
Provides:	perl(Wx::AuiManager)
Provides:	perl(Wx::AuiManagerEvent)
Provides:	perl(Wx::AuiNotebook)
Provides:	perl(Wx::AuiNotebookEvent)
Provides:	perl(Wx::AuiPaneInfo)
Provides:	perl(Wx::AutoBufferedPaintDC)
Provides:	perl(Wx::BMPHandler)
Provides:	perl(Wx::BannerWindow)
Provides:	perl(Wx::BestHelpController)
Provides:	perl(Wx::Bitmap)
Provides:	perl(Wx::BitmapButton)
Provides:	perl(Wx::BitmapComboBox)
Provides:	perl(Wx::BitmapDataObject)
Provides:	perl(Wx::BitmapToggleButton)
Provides:	perl(Wx::BookCtrl)
Provides:	perl(Wx::BookCtrlEvent)
Provides:	perl(Wx::BoolProperty)
Provides:	perl(Wx::BoxSizer)
Provides:	perl(Wx::Brush)
Provides:	perl(Wx::BufferedDC)
Provides:	perl(Wx::BufferedPaintDC)
Provides:	perl(Wx::BusyCursor)
Provides:	perl(Wx::BusyInfo)
Provides:	perl(Wx::Button)
Provides:	perl(Wx::CHMHelpController)
Provides:	perl(Wx::CURHandler)
Provides:	perl(Wx::CalendarCtrl)
Provides:	perl(Wx::CalendarDateAttr)
Provides:	perl(Wx::CalendarEvent)
Provides:	perl(Wx::Caret)
Provides:	perl(Wx::CaretSuspend)
Provides:	perl(Wx::CheckBox)
Provides:	perl(Wx::CheckListBox)
Provides:	perl(Wx::ChildFocusEvent)
Provides:	perl(Wx::Choice)
Provides:	perl(Wx::Choicebook)
Provides:	perl(Wx::ClassInfo)
Provides:	perl(Wx::ClassInfo)
Provides:	perl(Wx::Client)
Provides:	perl(Wx::ClientDC)
Provides:	perl(Wx::Clipboard)
Provides:	perl(Wx::ClipboardTextEvent)
Provides:	perl(Wx::CloseEvent)
Provides:	perl(Wx::CollapsiblePane)
Provides:	perl(Wx::CollapsiblePaneEvent)
Provides:	perl(Wx::Colour)
Provides:	perl(Wx::ColourData)
Provides:	perl(Wx::ColourDatabase)
Provides:	perl(Wx::ColourDialog)
Provides:	perl(Wx::ColourPickerCtrl)
Provides:	perl(Wx::ColourPickerEvent)
Provides:	perl(Wx::ColourProperty)
Provides:	perl(Wx::ColourPropertyValue)
Provides:	perl(Wx::ComboBox)
Provides:	perl(Wx::ComboCtrl)
Provides:	perl(Wx::ComboPopup)
Provides:	perl(Wx::Command)
Provides:	perl(Wx::CommandEvent)
Provides:	perl(Wx::CommandLinkButton)
Provides:	perl(Wx::CommandProcessor)
Provides:	perl(Wx::ConfigBase)
Provides:	perl(Wx::Connection)
Provides:	perl(Wx::ContextHelp)
Provides:	perl(Wx::ContextHelpButton)
Provides:	perl(Wx::ContextMenuEvent)
Provides:	perl(Wx::Control)
Provides:	perl(Wx::ControlWithItems)
Provides:	perl(Wx::Cursor)
Provides:	perl(Wx::CursorProperty)
Provides:	perl(Wx::DC)
Provides:	perl(Wx::DCClipper)
Provides:	perl(Wx::DCOverlay)
Provides:	perl(Wx::DataFormat)
Provides:	perl(Wx::DataObject)
Provides:	perl(Wx::DataObjectComposite)
Provides:	perl(Wx::DataObjectSimple)
Provides:	perl(Wx::DataView)
Provides:	perl(Wx::DataViewBitmapRenderer)
Provides:	perl(Wx::DataViewColumn)
Provides:	perl(Wx::DataViewCtrl)
Provides:	perl(Wx::DataViewDateRenderer)
Provides:	perl(Wx::DataViewEvent)
Provides:	perl(Wx::DataViewIconText)
Provides:	perl(Wx::DataViewIconTextRenderer)
Provides:	perl(Wx::DataViewIndexListModel)
Provides:	perl(Wx::DataViewItem)
Provides:	perl(Wx::DataViewItemAttr)
Provides:	perl(Wx::DataViewListCtrl)
Provides:	perl(Wx::DataViewListStore)
Provides:	perl(Wx::DataViewModel)
Provides:	perl(Wx::DataViewModelNotifier)
Provides:	perl(Wx::DataViewProgressRenderer)
Provides:	perl(Wx::DataViewRenderer)
Provides:	perl(Wx::DataViewSpinRenderer)
Provides:	perl(Wx::DataViewTextRenderer)
Provides:	perl(Wx::DataViewTextRendererAttr)
Provides:	perl(Wx::DataViewToggleRenderer)
Provides:	perl(Wx::DataViewTreeCtrl)
Provides:	perl(Wx::DataViewTreeStore)
Provides:	perl(Wx::DataViewVirtualListModel)
Provides:	perl(Wx::DatagramSocket)
Provides:	perl(Wx::DateEvent)
Provides:	perl(Wx::DatePickerCtrl)
Provides:	perl(Wx::DateProperty)
Provides:	perl(Wx::DateSpan)
Provides:	perl(Wx::DateTime)
Provides:	perl(Wx::Dialog)
Provides:	perl(Wx::DirDialog)
Provides:	perl(Wx::DirPickerCtrl)
Provides:	perl(Wx::DirProperty)
Provides:	perl(Wx::Display)
Provides:	perl(Wx::DocChildFrame)
Provides:	perl(Wx::DocMDIChildFrame)
Provides:	perl(Wx::DocMDIParentFrame)
Provides:	perl(Wx::DocManager)
Provides:	perl(Wx::DocParentFrame)
Provides:	perl(Wx::DocTemplate)
Provides:	perl(Wx::Document)
Provides:	perl(Wx::DropFilesEvent)
Provides:	perl(Wx::DropSource)
Provides:	perl(Wx::DropTarget)
Provides:	perl(Wx::EditEnumProperty)
Provides:	perl(Wx::EditableListBox)
Provides:	perl(Wx::EnumProperty)
Provides:	perl(Wx::EraseEvent)
Provides:	perl(Wx::Event)
Provides:	perl(Wx::EventBlocker)
Provides:	perl(Wx::EventFilter)
Provides:	perl(Wx::EvtHandler)
Provides:	perl(Wx::FSFile)
Provides:	perl(Wx::FileConfig)
Provides:	perl(Wx::FileCtrl)
Provides:	perl(Wx::FileCtrlEvent)
Provides:	perl(Wx::FileDataObject)
Provides:	perl(Wx::FileDialog)
Provides:	perl(Wx::FileDirPickerEvent)
Provides:	perl(Wx::FileDropTarget)
Provides:	perl(Wx::FileHistory)
Provides:	perl(Wx::FilePickerCtrl)
Provides:	perl(Wx::FileProperty)
Provides:	perl(Wx::FileSystem)
Provides:	perl(Wx::FileSystemHandler)
Provides:	perl(Wx::FileType)
Provides:	perl(Wx::FileTypeInfo)
Provides:	perl(Wx::FindDialogEvent)
Provides:	perl(Wx::FindReplaceData)
Provides:	perl(Wx::FindReplaceDialog)
Provides:	perl(Wx::FlagsProperty)
Provides:	perl(Wx::FlexGridSizer)
Provides:	perl(Wx::FlexGridSizer)
Provides:	perl(Wx::FloatProperty)
Provides:	perl(Wx::FocusEvent)
Provides:	perl(Wx::Font)
Provides:	perl(Wx::FontData)
Provides:	perl(Wx::FontDialog)
Provides:	perl(Wx::FontEnumerator)
Provides:	perl(Wx::FontEnumerator)
Provides:	perl(Wx::FontMapper)
Provides:	perl(Wx::FontPickerCtrl)
Provides:	perl(Wx::FontPickerEvent)
Provides:	perl(Wx::FontProperty)
Provides:	perl(Wx::Frame)
Provides:	perl(Wx::GBPosition)
Provides:	perl(Wx::GBSizerItem)
Provides:	perl(Wx::GBSpan)
Provides:	perl(Wx::GCDC)
Provides:	perl(Wx::GIFHandler)
Provides:	perl(Wx::Gauge)
Provides:	perl(Wx::GenericDirCtrl)
Provides:	perl(Wx::GraphicsBrush)
Provides:	perl(Wx::GraphicsContext)
Provides:	perl(Wx::GraphicsFont)
Provides:	perl(Wx::GraphicsGradientStop)
Provides:	perl(Wx::GraphicsGradientStops)
Provides:	perl(Wx::GraphicsMatrix)
Provides:	perl(Wx::GraphicsObject)
Provides:	perl(Wx::GraphicsPath)
Provides:	perl(Wx::GraphicsPen)
Provides:	perl(Wx::GraphicsRenderer)
Provides:	perl(Wx::Grid)
Provides:	perl(Wx::GridBagSizer)
Provides:	perl(Wx::GridBagSizer)
Provides:	perl(Wx::GridCellAttr)
Provides:	perl(Wx::GridCellAutoWrapStringEditor)
Provides:	perl(Wx::GridCellAutoWrapStringRenderer)
Provides:	perl(Wx::GridCellBoolEditor)
Provides:	perl(Wx::GridCellBoolRenderer)
Provides:	perl(Wx::GridCellChoiceEditor)
Provides:	perl(Wx::GridCellCoords)
Provides:	perl(Wx::GridCellDateTimeRenderer)
Provides:	perl(Wx::GridCellEditor)
Provides:	perl(Wx::GridCellEnumEditor)
Provides:	perl(Wx::GridCellEnumRenderer)
Provides:	perl(Wx::GridCellFloatEditor)
Provides:	perl(Wx::GridCellFloatRenderer)
Provides:	perl(Wx::GridCellNumberEditor)
Provides:	perl(Wx::GridCellNumberRenderer)
Provides:	perl(Wx::GridCellRenderer)
Provides:	perl(Wx::GridCellStringRenderer)
Provides:	perl(Wx::GridCellTextEditor)
Provides:	perl(Wx::GridEditorCreatedEvent)
Provides:	perl(Wx::GridEvent)
Provides:	perl(Wx::GridRangeSelectEvent)
Provides:	perl(Wx::GridSizeEvent)
Provides:	perl(Wx::GridSizer)
Provides:	perl(Wx::GridTableBase)
Provides:	perl(Wx::GridTableMessage)
Provides:	perl(Wx::GridUpdateLocker)
Provides:	perl(Wx::HScrolledWindow)
Provides:	perl(Wx::HVScrolledWindow)
Provides:	perl(Wx::HeaderColumn)
Provides:	perl(Wx::HeaderColumnSimple)
Provides:	perl(Wx::HeaderCtrl)
Provides:	perl(Wx::HeaderCtrlEvent)
Provides:	perl(Wx::HeaderCtrlSimple)
Provides:	perl(Wx::HelpControllerBase)
Provides:	perl(Wx::HelpControllerHelpProvider)
Provides:	perl(Wx::HelpEvent)
Provides:	perl(Wx::HelpProvider)
Provides:	perl(Wx::HtmlCell)
Provides:	perl(Wx::HtmlCellEvent)
Provides:	perl(Wx::HtmlColourCell)
Provides:	perl(Wx::HtmlContainerCell)
Provides:	perl(Wx::HtmlDCRenderer)
Provides:	perl(Wx::HtmlEasyPrinting)
Provides:	perl(Wx::HtmlFontCell)
Provides:	perl(Wx::HtmlHelpController)
Provides:	perl(Wx::HtmlLinkEvent)
Provides:	perl(Wx::HtmlLinkInfo)
Provides:	perl(Wx::HtmlListBox)
Provides:	perl(Wx::HtmlParser)
Provides:	perl(Wx::HtmlPrintout)
Provides:	perl(Wx::HtmlTag)
Provides:	perl(Wx::HtmlTagHandler)
Provides:	perl(Wx::HtmlWidgetCell)
Provides:	perl(Wx::HtmlWinParser)
Provides:	perl(Wx::HtmlWinTagHandler)
Provides:	perl(Wx::HtmlWindow)
Provides:	perl(Wx::HtmlWordCell)
Provides:	perl(Wx::HyperlinkCtrl)
Provides:	perl(Wx::HyperlinkEvent)
Provides:	perl(Wx::ICOHandler)
Provides:	perl(Wx::IFFHandler)
Provides:	perl(Wx::IPV4address)
Provides:	perl(Wx::IPV6address)
Provides:	perl(Wx::IPaddress)
Provides:	perl(Wx::Icon)
Provides:	perl(Wx::IconBundle)
Provides:	perl(Wx::IconLocation)
Provides:	perl(Wx::IconizeEvent)
Provides:	perl(Wx::IdleEvent)
Provides:	perl(Wx::Image)
Provides:	perl(Wx::ImageFileProperty)
Provides:	perl(Wx::ImageHandler)
Provides:	perl(Wx::ImageList)
Provides:	perl(Wx::ImageList)
Provides:	perl(Wx::IndividualLayoutConstraint)
Provides:	perl(Wx::InfoBar)
Provides:	perl(Wx::InitDialogEvent)
Provides:	perl(Wx::InputStream)
Provides:	perl(Wx::IntProperty)
Provides:	perl(Wx::InternetFSHandler)
Provides:	perl(Wx::ItemContainer)
Provides:	perl(Wx::ItemContainer)
Provides:	perl(Wx::ItemContainerImmutable)
Provides:	perl(Wx::ItemContainerImmutable)
Provides:	perl(Wx::JPEGHandler)
Provides:	perl(Wx::JoystickEvent)
Provides:	perl(Wx::KeyEvent)
Provides:	perl(Wx::LanguageInfo)
Provides:	perl(Wx::LayoutConstraints)
Provides:	perl(Wx::ListBox)
Provides:	perl(Wx::ListCtrl)
Provides:	perl(Wx::ListEvent)
Provides:	perl(Wx::ListItem)
Provides:	perl(Wx::ListItemAttr)
Provides:	perl(Wx::ListView)
Provides:	perl(Wx::Listbook)
Provides:	perl(Wx::Locale)
Provides:	perl(Wx::Log)
Provides:	perl(Wx::LogChain)
Provides:	perl(Wx::LogFormatter)
Provides:	perl(Wx::LogGui)
Provides:	perl(Wx::LogNull)
Provides:	perl(Wx::LogPassThrough)
Provides:	perl(Wx::LogRecordInfo)
Provides:	perl(Wx::LogStderr)
Provides:	perl(Wx::LogTextCtrl)
Provides:	perl(Wx::LogWindow)
Provides:	perl(Wx::LongStringProperty)
Provides:	perl(Wx::MDIChildFrame)
Provides:	perl(Wx::MDIParentFrame)
Provides:	perl(Wx::Mask)
Provides:	perl(Wx::MaximizeEvent)
Provides:	perl(Wx::MediaCtrl)
Provides:	perl(Wx::MediaEvent)
Provides:	perl(Wx::MemoryDC)
Provides:	perl(Wx::MemoryFSHandler)
Provides:	perl(Wx::Menu)
Provides:	perl(Wx::MenuBar)
Provides:	perl(Wx::MenuEvent)
Provides:	perl(Wx::MenuItem)
Provides:	perl(Wx::MessageDialog)
Provides:	perl(Wx::MimeTypesManager)
Provides:	perl(Wx::MiniFrame)
Provides:	perl(Wx::MirrorDC)
Provides:	perl(Wx::MouseCaptureChangedEvent)
Provides:	perl(Wx::MouseCaptureLostEvent)
Provides:	perl(Wx::MouseEvent)
Provides:	perl(Wx::MoveEvent)
Provides:	perl(Wx::MultiChoiceDialog)
Provides:	perl(Wx::MultiChoiceProperty)
Provides:	perl(Wx::NativeFontInfo)
Provides:	perl(Wx::NavigationKeyEvent)
Provides:	perl(Wx::NewClass)
Provides:	perl(Wx::NewClass)
Provides:	perl(Wx::Notebook)
Provides:	perl(Wx::NotebookEvent)
Provides:	perl(Wx::NotebookSizer)
Provides:	perl(Wx::NotificationMessage)
Provides:	perl(Wx::NotifyEvent)
Provides:	perl(Wx::NumberEntryDialog)
Provides:	perl(Wx::OutputStream)
Provides:	perl(Wx::Overlay)
Provides:	perl(Wx::OwnerDrawnComboBox)
Provides:	perl(Wx::PCXHandler)
Provides:	perl(Wx::PGArrayEditorDialog)
Provides:	perl(Wx::PGArrayStringEditorDialog)
Provides:	perl(Wx::PGCell)
Provides:	perl(Wx::PGCellRenderer)
Provides:	perl(Wx::PGCheckBoxEditor)
Provides:	perl(Wx::PGChoiceAndButtonEditor)
Provides:	perl(Wx::PGChoiceEditor)
Provides:	perl(Wx::PGChoiceEntry)
Provides:	perl(Wx::PGChoices)
Provides:	perl(Wx::PGChoicesData)
Provides:	perl(Wx::PGComboBoxEditor)
Provides:	perl(Wx::PGDatePickerCtrlEditor)
Provides:	perl(Wx::PGEditor)
Provides:	perl(Wx::PGEditorDialogAdapter)
Provides:	perl(Wx::PGFileDialogAdapter)
Provides:	perl(Wx::PGLongStringDialogAdapter)
Provides:	perl(Wx::PGMultiButton)
Provides:	perl(Wx::PGPGridInterfaceBase)
Provides:	perl(Wx::PGPGridInterfaceBase)
Provides:	perl(Wx::PGProperty)
Provides:	perl(Wx::PGSpinCtrlEditor)
Provides:	perl(Wx::PGTextCtrlAndButtonEditor)
Provides:	perl(Wx::PGTextCtrlEditor)
Provides:	perl(Wx::PGVIterator)
Provides:	perl(Wx::PGValidationInfo)
Provides:	perl(Wx::PGWindowList)
Provides:	perl(Wx::PNGHandler)
Provides:	perl(Wx::PNMHandler)
Provides:	perl(Wx::PageSetupDialog)
Provides:	perl(Wx::PageSetupDialogData)
Provides:	perl(Wx::PaintDC)
Provides:	perl(Wx::PaintEvent)
Provides:	perl(Wx::Palette)
Provides:	perl(Wx::Panel)
Provides:	perl(Wx::PasswordEntryDialog)
Provides:	perl(Wx::Pen)
Provides:	perl(Wx::PerlTestAbstractNonObject)
Provides:	perl(Wx::PerlTestAbstractObject)
Provides:	perl(Wx::PerlTestNonObject)
Provides:	perl(Wx::PerlTestObject)
Provides:	perl(Wx::PickerBase)
Provides:	perl(Wx::PlArtProvider)
Provides:	perl(Wx::PlArtProvider)
Provides:	perl(Wx::PlCommand)
Provides:	perl(Wx::PlCommandEvent)
Provides:	perl(Wx::PlDataObjectSimple)
Provides:	perl(Wx::PlDataViewIndexListModel)
Provides:	perl(Wx::PlEvent)
Provides:	perl(Wx::PlEventFilter)
Provides:	perl(Wx::PlFileSystemHandler)
Provides:	perl(Wx::PlGridCellEditor)
Provides:	perl(Wx::PlGridCellRenderer)
Provides:	perl(Wx::PlHScrolledWindow)
Provides:	perl(Wx::PlHVScrolledWindow)
Provides:	perl(Wx::PlHtmlListBox)
Provides:	perl(Wx::PlHtmlTagHandler)
Provides:	perl(Wx::PlHtmlWinTagHandler)
Provides:	perl(Wx::PlLog)
Provides:	perl(Wx::PlLogFormatter)
Provides:	perl(Wx::PlLogPassThrough)
Provides:	perl(Wx::PlOwnerDrawnComboBox)
Provides:	perl(Wx::PlPopupTransientWindow)
Provides:	perl(Wx::PlPreviewControlBar)
Provides:	perl(Wx::PlPreviewFrame)
Provides:	perl(Wx::PlRichTextFileHandler)
Provides:	perl(Wx::PlSizer)
Provides:	perl(Wx::PlThreadEvent)
Provides:	perl(Wx::PlVListBox)
Provides:	perl(Wx::PlVScrolledWindow)
Provides:	perl(Wx::PlValidator)
Provides:	perl(Wx::PlWindow)
Provides:	perl(Wx::PlXmlResourceHandler)
Provides:	perl(Wx::Point)
Provides:	perl(Wx::PopupTransientWindow)
Provides:	perl(Wx::PopupWindow)
Provides:	perl(Wx::Position)
Provides:	perl(Wx::PowerEvent)
Provides:	perl(Wx::PreviewCanvas)
Provides:	perl(Wx::PreviewControlBar)
Provides:	perl(Wx::PreviewFrame)
Provides:	perl(Wx::PrintData)
Provides:	perl(Wx::PrintDialog)
Provides:	perl(Wx::PrintDialogData)
Provides:	perl(Wx::PrintFactory)
Provides:	perl(Wx::PrintFactory)
Provides:	perl(Wx::PrintPaperDatabase)
Provides:	perl(Wx::PrintPaperType)
Provides:	perl(Wx::PrintPreview)
Provides:	perl(Wx::Printer)
Provides:	perl(Wx::PrinterDC)
Provides:	perl(Wx::Printout)
Provides:	perl(Wx::Process)
Provides:	perl(Wx::ProcessEvent)
Provides:	perl(Wx::ProgressDialog)
Provides:	perl(Wx::PropertyAccessor)
Provides:	perl(Wx::PropertyCategory)
Provides:	perl(Wx::PropertyGrid)
Provides:	perl(Wx::PropertyGrid)
Provides:	perl(Wx::PropertyGridEvent)
Provides:	perl(Wx::PropertyGridHitTestResult)
Provides:	perl(Wx::PropertyGridIterator)
Provides:	perl(Wx::PropertyGridManager)
Provides:	perl(Wx::PropertyGridPage)
Provides:	perl(Wx::PropertyInfo)
Provides:	perl(Wx::PropertySheetDialog)
Provides:	perl(Wx::RadioBox)
Provides:	perl(Wx::RadioButton)
Provides:	perl(Wx::RearrangeCtrl)
Provides:	perl(Wx::RearrangeDialog)
Provides:	perl(Wx::RearrangeList)
Provides:	perl(Wx::Rect)
Provides:	perl(Wx::RegConfig)
Provides:	perl(Wx::Region)
Provides:	perl(Wx::RegionIterator)
Provides:	perl(Wx::Ribbon)
Provides:	perl(Wx::RibbonAUIArtProvider)
Provides:	perl(Wx::RibbonArtProvider)
Provides:	perl(Wx::RibbonBar)
Provides:	perl(Wx::RibbonBarEvent)
Provides:	perl(Wx::RibbonButtonBar)
Provides:	perl(Wx::RibbonButtonBarButtonBase)
Provides:	perl(Wx::RibbonButtonBarEvent)
Provides:	perl(Wx::RibbonControl)
Provides:	perl(Wx::RibbonGallery)
Provides:	perl(Wx::RibbonGalleryEvent)
Provides:	perl(Wx::RibbonGalleryItem)
Provides:	perl(Wx::RibbonMSWArtProvider)
Provides:	perl(Wx::RibbonPage)
Provides:	perl(Wx::RibbonPanel)
Provides:	perl(Wx::RibbonToolBar)
Provides:	perl(Wx::RibbonToolBarEvent)
Provides:	perl(Wx::RibbonToolBarToolBase)
Provides:	perl(Wx::RichText)
Provides:	perl(Wx::RichTextAttr)
Provides:	perl(Wx::RichTextBuffer)
Provides:	perl(Wx::RichTextCharacterStyleDefinition)
Provides:	perl(Wx::RichTextCtrl)
Provides:	perl(Wx::RichTextEvent)
Provides:	perl(Wx::RichTextFileHandler)
Provides:	perl(Wx::RichTextFormattingDialog)
Provides:	perl(Wx::RichTextHTMLHandler)
Provides:	perl(Wx::RichTextHeaderFooterData)
Provides:	perl(Wx::RichTextListStyleDefinition)
Provides:	perl(Wx::RichTextParagraphStyleDefinition)
Provides:	perl(Wx::RichTextPrinting)
Provides:	perl(Wx::RichTextPrintout)
Provides:	perl(Wx::RichTextRange)
Provides:	perl(Wx::RichTextStyleComboCtrl)
Provides:	perl(Wx::RichTextStyleDefinition)
Provides:	perl(Wx::RichTextStyleListBox)
Provides:	perl(Wx::RichTextStyleListCtrl)
Provides:	perl(Wx::RichTextStyleOrganiserDialog)
Provides:	perl(Wx::RichTextStyleSheet)
Provides:	perl(Wx::RichTextXMLHandler)
Provides:	perl(Wx::RichToolTip)
Provides:	perl(Wx::SVGFileDC)
Provides:	perl(Wx::SashEvent)
Provides:	perl(Wx::SashWindow)
Provides:	perl(Wx::ScreenDC)
Provides:	perl(Wx::ScrollBar)
Provides:	perl(Wx::ScrollEvent)
Provides:	perl(Wx::ScrollWinEvent)
Provides:	perl(Wx::ScrolledWindow)
Provides:	perl(Wx::SearchCtrl)
Provides:	perl(Wx::Server)
Provides:	perl(Wx::SetCursorEvent)
Provides:	perl(Wx::SettableHeaderColumn)
Provides:	perl(Wx::SimpleHelpProvider)
Provides:	perl(Wx::SimpleHtmlListBox)
Provides:	perl(Wx::SingleChoiceDialog)
Provides:	perl(Wx::SingleInstanceChecker)
Provides:	perl(Wx::Size)
Provides:	perl(Wx::SizeEvent)
Provides:	perl(Wx::Sizer)
Provides:	perl(Wx::Sizer)
Provides:	perl(Wx::SizerItem)
Provides:	perl(Wx::SizerItem)
Provides:	perl(Wx::Slider)
Provides:	perl(Wx::SockAddress)
Provides:	perl(Wx::SocketBase)
Provides:	perl(Wx::SocketClient)
Provides:	perl(Wx::SocketEvent)
Provides:	perl(Wx::SocketServer)
Provides:	perl(Wx::Sound)
Provides:	perl(Wx::SpinButton)
Provides:	perl(Wx::SpinCtrl)
Provides:	perl(Wx::SpinCtrlDouble)
Provides:	perl(Wx::SpinEvent)
Provides:	perl(Wx::SplashScreen)
Provides:	perl(Wx::SplitterEvent)
Provides:	perl(Wx::SplitterWindow)
Provides:	perl(Wx::StandardPaths)
Provides:	perl(Wx::StaticBitmap)
Provides:	perl(Wx::StaticBox)
Provides:	perl(Wx::StaticBoxSizer)
Provides:	perl(Wx::StaticLine)
Provides:	perl(Wx::StaticText)
Provides:	perl(Wx::StatusBar)
Provides:	perl(Wx::StdDialogButtonSizer)
Provides:	perl(Wx::StopWatch)
Provides:	perl(Wx::Stream)
Provides:	perl(Wx::StringProperty)
Provides:	perl(Wx::StyledTextCtrl)
Provides:	perl(Wx::StyledTextEvent)
Provides:	perl(Wx::SymbolPickerDialog)
Provides:	perl(Wx::SysColourChangedEvent)
Provides:	perl(Wx::SystemColourProperty)
Provides:	perl(Wx::SystemOptions)
Provides:	perl(Wx::SystemSettings)
Provides:	perl(Wx::TGAHandler)
Provides:	perl(Wx::TIFFHandler)
Provides:	perl(Wx::TaskBarIcon)
Provides:	perl(Wx::TaskBarIconEvent)
Provides:	perl(Wx::TextAttr)
Provides:	perl(Wx::TextAttrEx)
Provides:	perl(Wx::TextCtrl)
Provides:	perl(Wx::TextCtrlBase)
Provides:	perl(Wx::TextCtrlIface)
Provides:	perl(Wx::TextCtrlIface)
Provides:	perl(Wx::TextDataObject)
Provides:	perl(Wx::TextDropTarget)
Provides:	perl(Wx::TextEntryDialog)
Provides:	perl(Wx::TextUrlEvent)
Provides:	perl(Wx::Thread)
Provides:	perl(Wx::TimePickerCtrl)
Provides:	perl(Wx::TimeSpan)
Provides:	perl(Wx::Timer)
Provides:	perl(Wx::TimerEvent)
Provides:	perl(Wx::TipProvider)
Provides:	perl(Wx::ToggleButton)
Provides:	perl(Wx::ToolBar)
Provides:	perl(Wx::ToolBarBase)
Provides:	perl(Wx::ToolBarToolBase)
Provides:	perl(Wx::ToolTip)
Provides:	perl(Wx::Toolbook)
Provides:	perl(Wx::TopLevelWindow)
Provides:	perl(Wx::TreeCtrl)
Provides:	perl(Wx::TreeEvent)
Provides:	perl(Wx::TreeItemData)
Provides:	perl(Wx::TreeItemId)
Provides:	perl(Wx::TreeListCtrl)
Provides:	perl(Wx::TreeListEvent)
Provides:	perl(Wx::TreeListItem)
Provides:	perl(Wx::TreeListItemComparator)
Provides:	perl(Wx::Treebook)
Provides:	perl(Wx::TreebookEvent)
Provides:	perl(Wx::TypeInfo)
Provides:	perl(Wx::UIActionSimulator)
Provides:	perl(Wx::UIntProperty)
Provides:	perl(Wx::UNIXaddress)
Provides:	perl(Wx::URLDataObject)
Provides:	perl(Wx::UpdateUIEvent)
Provides:	perl(Wx::VListBox)
Provides:	perl(Wx::VScrolledWindow)
Provides:	perl(Wx::Validator)
Provides:	perl(Wx::VarHScrollHelper)
Provides:	perl(Wx::VarHScrollHelper)
Provides:	perl(Wx::VarHVScrollHelper)
Provides:	perl(Wx::VarHVScrollHelper)
Provides:	perl(Wx::VarScrollHelperBase)
Provides:	perl(Wx::VarScrollHelperBase)
Provides:	perl(Wx::VarVScrollHelper)
Provides:	perl(Wx::VarVScrollHelper)
Provides:	perl(Wx::Variant)
Provides:	perl(Wx::VideoMode)
Provides:	perl(Wx::View)
Provides:	perl(Wx::Wave)
Provides:	perl(Wx::WebView)
Provides:	perl(Wx::WebView)
Provides:	perl(Wx::WebView)
Provides:	perl(Wx::WebViewArchiveHandler)
Provides:	perl(Wx::WebViewArchiveHandler)
Provides:	perl(Wx::WebViewEvent)
Provides:	perl(Wx::WebViewEvent)
Provides:	perl(Wx::WebViewHandler)
Provides:	perl(Wx::WebViewHandler)
Provides:	perl(Wx::WebViewHistoryItem)
Provides:	perl(Wx::WebViewHistoryItem)
Provides:	perl(Wx::WinHelpController)
Provides:	perl(Wx::Window)
Provides:	perl(Wx::Window)
Provides:	perl(Wx::WindowCreateEvent)
Provides:	perl(Wx::WindowDC)
Provides:	perl(Wx::WindowDestroyEvent)
Provides:	perl(Wx::WindowDisabler)
Provides:	perl(Wx::WindowUpdateLocker)
Provides:	perl(Wx::Wizard)
Provides:	perl(Wx::WizardEvent)
Provides:	perl(Wx::WizardPage)
Provides:	perl(Wx::WizardPageSimple)
Provides:	perl(Wx::WrapSizer)
Provides:	perl(Wx::XPMHandler)
Provides:	perl(Wx::XmlAttribute)
Provides:	perl(Wx::XmlDocument)
Provides:	perl(Wx::XmlNode)
Provides:	perl(Wx::XmlProperty)
Provides:	perl(Wx::XmlResource)
Provides:	perl(Wx::XmlResourceHandler)
Provides:	perl(Wx::XmlSubclassFactory)
Provides:	perl(Wx::ZipFSHandler)
Provides:	perl(Wx::_App)

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
