# Why not store the SAFEARRAY reference count as a hidden allocation next to the SAFEARRAY?

**来源:** https://devblogs.microsoft.com_oldnewthing
**链接:** https://devblogs.microsoft.com/oldnewthing/20260130-00/?p=112025
**日期:** Fri, 30 Jan 2026 15:00:00 +0000

---

[Skip to main content](javascript:void\(0\))

[ ![](https://uhf.microsoft.com/images/microsoft/RE1Mu3b.png) Microsoft ](https://www.microsoft.com)

Dev Blogs

[ Dev Blogs ](https://devblogs.microsoft.com)

Dev Blogs 

  * [ Home ](https://devblogs.microsoft.com)
  * Developer
    * [Microsoft for Developers](https://developer.microsoft.com/blog)
    * [Visual Studio](https://devblogs.microsoft.com/visualstudio/)
    * [Visual Studio Code](https://devblogs.microsoft.com/vscode-blog)
    * [Develop from the cloud](https://devblogs.microsoft.com/develop-from-the-cloud/)
    * [All things Azure](https://devblogs.microsoft.com/all-things-azure/)
    * [Xcode](https://devblogs.microsoft.com/xcode/)
    * [DevOps](https://devblogs.microsoft.com/devops/)
    * [Windows Developer](https://blogs.windows.com/windowsdeveloper/)
    * [ISE Developer](https://devblogs.microsoft.com/ise/)
    * [Azure SDK](https://devblogs.microsoft.com/azure-sdk/)
    * [Command Line](https://devblogs.microsoft.com/commandline/)
    * [Aspire](https://devblogs.microsoft.com/aspire/)

  * Technology
    * [DirectX](https://devblogs.microsoft.com/directx/)
    * [Semantic Kernel](https://devblogs.microsoft.com/semantic-kernel/)

  * Languages
    * [C++](https://devblogs.microsoft.com/cppblog/)
    * [C#](https://devblogs.microsoft.com/dotnet/category/csharp/)
    * [F#](https://devblogs.microsoft.com/dotnet/category/fsharp/)
    * [TypeScript](https://devblogs.microsoft.com/typescript/)
    * [PowerShell Team](https://devblogs.microsoft.com/powershell/)
    * [Python](https://devblogs.microsoft.com/python/)
    * [Java](https://devblogs.microsoft.com/java/)
    * [Java Blog in Chinese](https://devblogs.microsoft.com/java-ch/)
    * [Go](https://devblogs.microsoft.com/go/)

  * .NET
    * [All .NET posts](https://devblogs.microsoft.com/dotnet/ )
    * [.NET Aspire](https://devblogs.microsoft.com/dotnet/category/dotnet-aspire/)
    * [.NET MAUI](https://devblogs.microsoft.com/dotnet/category/maui/)
    * [AI](https://devblogs.microsoft.com/dotnet/category/ai/)
    * [ASP.NET Core](https://devblogs.microsoft.com/dotnet/category/aspnetcore/)
    * [Blazor](https://devblogs.microsoft.com/dotnet/category/blazor/)
    * [Entity Framework](https://devblogs.microsoft.com/dotnet/category/entity-framework/)
    * [NuGet](https://devblogs.microsoft.com/dotnet/category/nuget/)
    * [Servicing](https://devblogs.microsoft.com/dotnet/category/maintenance-and-updates/)
    * [.NET Blog in Chinese](https://devblogs.microsoft.com/dotnet-ch/)

  * Platform Development
    * [#ifdef Windows](https://devblogs.microsoft.com/ifdef-windows/)
    * [Microsoft Foundry](https://devblogs.microsoft.com/foundry/)
    * [Azure Government](https://devblogs.microsoft.com/azuregov/)
    * [Azure VM Runtime Team](https://devblogs.microsoft.com/azure-vm-runtime/)
    * [Bing Dev Center](https://blogs.bing.com/Developers-Blog/)
    * [Microsoft Edge Dev](http://blogs.windows.com/msedgedev/)
    * [Microsoft Azure](http://azure.microsoft.com/blog/)
    * [Microsoft 365 Developer](https://devblogs.microsoft.com/microsoft365dev/)
    * [Microsoft Entra Identity Developer](https://devblogs.microsoft.com/identity/)
    * [Old New Thing](https://devblogs.microsoft.com/oldnewthing/)
    * [Power Platform](https://devblogs.microsoft.com/powerplatform/)

  * Data Development
    * [ Azure Cosmos DB](https://devblogs.microsoft.com/cosmosdb/)
    * [Azure Data Studio](https://cloudblogs.microsoft.com/sqlserver/?product=azure-data-studio)
    * [Azure SQL](https://devblogs.microsoft.com/azure-sql/)
    * [OData](https://devblogs.microsoft.com/odata/)
    * [Revolutions R](http://blog.revolutionanalytics.com/)
    * [Unified Data Model (IDEAs)](https://devblogs.microsoft.com/udm/)
    * [Microsoft Entra PowerShell](https://devblogs.microsoft.com/entrapowershell/)

  * More




Search Search



  * No results



Cancel

  * [Dev Blogs](https://devblogs.microsoft.com/)
  * [The Old New Thing](https://devblogs.microsoft.com/oldnewthing/)
  * Why not store the SAFEARRAY reference count as a hidden allocation next to the SAFEARRAY?



January 30th, 2026

![mind blown](https://devblogs.microsoft.com/oldnewthing/wp-content/themes/devblogs-evo/images/emojis/mind-blown.svg)1 reaction

# Why not store the `SAFEARRAY` reference count as a hidden allocation next to the `SAFEARRAY`?

![Raymond Chen](https://devblogs.microsoft.com/oldnewthing/wp-content/uploads/sites/38/2019/02/RaymondChen_5in-150x150.jpg)

[Raymond Chen](https://devblogs.microsoft.com/oldnewthing/author/oldnewthing)

## 


[Show more](javascript:)

When I described [ how `Safe­Array­Add­Ref` keeps its reference count in a side table](https://devblogs.microsoft.com/oldnewthing/20260127-00/?p=112018 "A digression on the design and implementation of SafeArrayAddRef and extending APIs in general"), commenter Koro Unhallowed wondered [ why we couldn't store the reference count either before or after the formal `SAFEARRAY` structure](https://devblogs.microsoft.com/oldnewthing/20260127-00/?p=112018&commentid=143776#comment-143776). Commenter Peter Cooper Jr. suspected that [ there might be cases where applications assumed how much memory a `SAFEARRAY` occupied](https://devblogs.microsoft.com/oldnewthing/20260127-00/?p=112018&commentid=143779#comment-143779).

And indeed that is the case.

Not all `SAFEARRAY`s are created by the `Safe­Array­Create` function. I've seen code that declared and filled out their own `SAFEARRAY` structure. In those cases, the code allocates exactly `sizeof(SAFEARRAY)` bytes and doesn't allocate any bonus data for the reference count.

Indeed, there three flags [ in the `fFeatures` member](https://learn.microsoft.com/windows/win32/api/oaidl/ns-oaidl-safearray) for these "bring your own `SAFEARRAY`" structures.

`FADF_AUTO` | An array that is allocated on the stack.  
---|---  
`FADF_STATIC` | An array that is statically allocated.  
`FADF_EMBEDDED` | An array that is embedded in a structure.  
  
These flag indicate that the array was not created by `Safe­Array­Create` but rather was constructed manually by the caller in various ways.¹

Note that if you pass a `SAFEARRAY` with one these flags to `Safe­Array­Add­Ref`, it will still increment the reference count, but you don't get a data pointer back because the caller does not control the lifetime of the `SAFEARRAY`. The lifetime of the `SAFEARRAY` is controlled by the lifetime of the `SAFEARRAY` variable on the stack (`FADF_AUTO`), in the DLL's global data segment (`FADF_STATIC`), or in the enclosing object (`FADF_EMBEDDED`).

This means that our earlier suggestion to wrap the `SAFEARRAY` inside an in/out `VARIANT` runs into trouble if the `SAFEARRAY` is one of these types of arrays with externally-controlled lifetime. For those, you have no choice but to copy the data.

¹ The documentation is, however, ambiguous about what "the array" refers to. Is it referring to the `SAFEARRAY` structure itself? Or is it referring to the data pointed to by the `pvData` member?

[ 1](https://devblogs.microsoft.com/oldnewthing/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Foldnewthing%2F20260130-00%2F%3Fp%3D112025 "Sign in to react")

  *   *   *   *   *   * 


1

1 

  * [ ![Facebook](https://devblogs.microsoft.com/oldnewthing/wp-content/themes/devblogs-evo/images/social-icons/facebook.svg) Share on Facebook ](https://www.facebook.com/sharer/sharer.php?u=https://devblogs.microsoft.com/oldnewthing/20260130-00/?p=112025 "Share on Facebook")
  * [ Share on X ](https://twitter.com/intent/tweet?url=https://devblogs.microsoft.com/oldnewthing/20260130-00/?p=112025&text=Why not store the <CODE>SAFEARRAY</CODE> reference count as a hidden allocation next to the <CODE>SAFEARRAY</CODE>? "Share on X")
  * [ ![LinkedIn](https://devblogs.microsoft.com/oldnewthing/wp-content/themes/devblogs-evo/images/social-icons/linkedin.svg) Share on Linkedin ](https://www.linkedin.com/shareArticle?mini=true&url=https://devblogs.microsoft.com/oldnewthing/20260130-00/?p=112025 "Share on LinkedIn")



Category

[Old New Thing](https://devblogs.microsoft.com/oldnewthing/category/oldnewthing)

Topics

[Code](https://devblogs.microsoft.com/oldnewthing/tag/code)

Share

  * [ ](https://www.facebook.com/sharer/sharer.php?u=https://devblogs.microsoft.com/oldnewthing/20260130-00/?p=112025)
  * [ ](https://twitter.com/intent/tweet?url=https://devblogs.microsoft.com/oldnewthing/20260130-00/?p=112025&text=Why not store the <CODE>SAFEARRAY</CODE> reference count as a hidden allocation next to the <CODE>SAFEARRAY</CODE>?)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https://devblogs.microsoft.com/oldnewthing/20260130-00/?p=112025)



## Author

![Raymond Chen](https://devblogs.microsoft.com/oldnewthing/wp-content/uploads/sites/38/2019/02/RaymondChen_5in-150x150.jpg)

[Raymond Chen](https://devblogs.microsoft.com/oldnewthing/author/oldnewthing)

Raymond has been involved in the evolution of Windows for more than 30 years. In 2003, he began a Web site known as The Old New Thing which has grown in popularity far beyond his wildest imagination, a development which still gives him the heebie-jeebies. The Web site spawned a book, coincidentally also titled The Old New Thing (Addison Wesley 2007). He occasionally appears on the Windows Dev Docs Twitter account to tell stories which convey no useful information.

##  1 comment 

Join the discussion.

### [Leave a comment](javascript:void\(0\) "Leave a comment")[Cancel reply](/oldnewthing/20260130-00/?p=112025#respond)

[Sign in](https://devblogs.microsoft.com/oldnewthing/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Foldnewthing%2F20260130-00%2F%3Fp%3D112025%23comments)

[Code of Conduct](https://aka.ms/msftqacodeconduct)

Sort by :

Newest

[Newest](javascript:void\(0\)) [Popular](javascript:void\(0\)) [Oldest](javascript:void\(0\))

  * ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAAAyAQMAAACQ++z9AAAAA1BMVEXW1taWrGEgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAD0lEQVQokWNgGAWjYGgCAAK8AAGBAoNpAAAAAElFTkSuQmCC)

Joshua Hudson  February 2, 2026  0

Collapse this comment Copy link

Methinks the SAFEARRAY document needs to be updated for 64 bit.

"An array that contains records. When set, there will be a pointer to the IRecordInfo interface at negative offset 4 in the array descriptor. "

For 64 bit this could mean three possible things:

1) The IRecordInfo needs to be allocated in the bottom 2GB of address space.  
2) The IRecordInfo needs to be allocated in the bottom 4GB of address space.  
3) …negative offset 8 in the array descriptor

[Log in to Vote or Reply](https://devblogs.microsoft.com/oldnewthing/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Foldnewthing%2F20260130-00%2F%3Fp%3D112025%23comments)




## Read next

February 2, 2026

### [Studying compiler error messages closely: Input file paths](https://devblogs.microsoft.com/oldnewthing/20260202-00/?p=112027)

![Raymond Chen](https://devblogs.microsoft.com/oldnewthing/wp-content/uploads/sites/38/2019/02/RaymondChen_5in-150x150.jpg)

Raymond Chen

February 4, 2026

### [How can I prevent the user from changing the widths of ListView columns?](https://devblogs.microsoft.com/oldnewthing/20260204-00/?p=112037)

![Raymond Chen](https://devblogs.microsoft.com/oldnewthing/wp-content/uploads/sites/38/2019/02/RaymondChen_5in-150x150.jpg)

Raymond Chen

## Stay informed

Get notified when new posts are published.

Email *

Country/Region * Select...United StatesAfghanistanÅland IslandsAlbaniaAlgeriaAmerican SamoaAndorraAngolaAnguillaAntarcticaAntigua and BarbudaArgentinaArmeniaArubaAustraliaAustriaAzerbaijanBahamasBahrainBangladeshBarbadosBelarusBelgiumBelizeBeninBermudaBhutanBoliviaBonaireBosnia and HerzegovinaBotswanaBouvet IslandBrazilBritish Indian Ocean TerritoryBritish Virgin IslandsBruneiBulgariaBurkina FasoBurundiCabo VerdeCambodiaCameroonCanadaCayman IslandsCentral African RepublicChadChileChinaChristmas IslandCocos (Keeling) IslandsColombiaComorosCongoCongo (DRC)Cook IslandsCosta RicaCôte dIvoireCroatiaCuraçaoCyprusCzechiaDenmarkDjiboutiDominicaDominican RepublicEcuadorEgyptEl SalvadorEquatorial GuineaEritreaEstoniaEswatiniEthiopiaFalkland IslandsFaroe IslandsFijiFinlandFranceFrench GuianaFrench PolynesiaFrench Southern TerritoriesGabonGambiaGeorgiaGermanyGhanaGibraltarGreeceGreenlandGrenadaGuadeloupeGuamGuatemalaGuernseyGuineaGuinea-BissauGuyanaHaitiHeard Island and McDonald IslandsHondurasHong Kong SARHungaryIcelandIndiaIndonesiaIraqIrelandIsle of ManIsraelItalyJamaicaJan MayenJapanJerseyJordanKazakhstanKenyaKiribatiKoreaKosovoKuwaitKyrgyzstanLaosLatviaLebanonLesothoLiberiaLibyaLiechtensteinLithuaniaLuxembourgMacau SARMadagascarMalawiMalaysiaMaldivesMaliMaltaMarshall IslandsMartiniqueMauritaniaMauritiusMayotteMexicoMicronesiaMoldovaMonacoMongoliaMontenegroMontserratMoroccoMozambiqueMyanmarNamibiaNauruNepalNetherlandsNew CaledoniaNew ZealandNicaraguaNigerNigeriaNiueNorfolk IslandNorth MacedoniaNorthern Mariana IslandsNorwayOmanPakistanPalauPalestinian AuthorityPanamaPapua New GuineaParaguayPeruPhilippinesPitcairn IslandsPolandPortugalPuerto RicoQatarRéunionRomaniaRwandaSabaSaint BarthélemySaint Kitts and NevisSaint LuciaSaint MartinSaint Pierre and MiquelonSaint Vincent and the GrenadinesSamoaSan MarinoSão Tomé and PríncipeSaudi ArabiaSenegalSerbiaSeychellesSierra LeoneSingaporeSint EustatiusSint MaartenSlovakiaSloveniaSolomon IslandsSomaliaSouth AfricaSouth Georgia and South Sandwich IslandsSouth SudanSpainSri LankaSt HelenaAscensionTristan da CunhaSurinameSvalbardSwedenSwitzerlandTaiwanTajikistanTanzaniaThailandTimor-LesteTogoTokelauTongaTrinidad and TobagoTunisiaTurkeyTurkmenistanTurks and Caicos IslandsTuvaluU.S. Outlying IslandsU.S. Virgin IslandsUgandaUkraineUnited Arab EmiratesUnited KingdomUruguayUzbekistanVanuatuVatican CityVenezuelaVietnamWallis and FutunaYemenZambiaZimbabwe

I would like to receive the The Old New Thing Newsletter. [Privacy Statement.](https://go.microsoft.com/fwlink/?LinkId=521839)

Subscribe

Follow this blog

[](https://twitter.com/ChenCravat "twitter")[![youtube](https://devblogs.microsoft.com/oldnewthing/wp-content/themes/devblogs-evo/images/social-icons/youtube.svg)](https://www.youtube.com/playlist?list=PLlrxD0HtieHge3_8Dm48C0Ns61I6bHThc "youtube")[](https://github.com/oldnewthing "GitHub")[](https://devblogs.microsoft.com/oldnewthing/feed/ "RSS Feed")

Are you sure you wish to delete this comment?

OK Cancel

[Sign in](https://devblogs.microsoft.com/oldnewthing/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Foldnewthing%2F20260130-00%2F%3Fp%3D112025)

Theme

# Insert/edit link

Close 

Enter the destination URL

URL

Link Text

Open link in a new tab

Or link to existing content

Search




_No search term specified. Showing recent items._ _Search or use up and down arrow keys to select an item._




Cancel

##### Code Block

×

Paste your code snippet

Ok Cancel

What's new

  * [Surface Pro](https://www.microsoft.com/surface/devices/surface-pro)
  * [Surface Laptop](https://www.microsoft.com/surface/devices/surface-laptop)
  * [Surface Laptop Studio 2](https://www.microsoft.com/en-us/d/Surface-Laptop-Studio-2/8rqr54krf1dz)
  * [Copilot for organizations](https://www.microsoft.com/en-us/microsoft-copilot/organizations?icid=DSM_Footer_CopilotOrganizations)
  * [Copilot for personal use](https://www.microsoft.com/en-us/microsoft-copilot/for-individuals?form=MY02PT&OCID=GE_web_Copilot_Free_868g3t5nj)
  * [AI in Windows](https://www.microsoft.com/en-us/windows/ai-features?icid=DSM_Footer_WhatsNew_AIinWindows)
  * [Explore Microsoft products](https://www.microsoft.com/en-us/microsoft-products-and-apps)
  * [Windows 11 apps](https://www.microsoft.com/en-us/windows/apps-for-windows?icid=DSM_Footer_WhatsNew_Windows11apps)



Microsoft Store

  * [Account profile](https://account.microsoft.com/)
  * [Download Center](https://www.microsoft.com/en-us/download)
  * [Microsoft Store support](https://go.microsoft.com/fwlink/?linkid=2139749)
  * [Returns](https://www.microsoft.com/en-us/store/b/returns)
  * [Order tracking](https://www.microsoft.com/en-us/store/b/order-tracking)
  * [Certified Refurbished](https://www.microsoft.com/en-us/store/b/certified-refurbished-products)
  * [Microsoft Store Promise](https://www.microsoft.com/en-us/store/b/why-microsoft-store?icid=footer_why-msft-store_7102020)
  * [Flexible Payments](https://www.microsoft.com/en-us/store/b/payment-financing-options?icid=footer_financing_vcc)



Education

  * [Microsoft in education](https://www.microsoft.com/en-us/education)
  * [Devices for education](https://www.microsoft.com/en-us/education/devices/overview)
  * [Microsoft Teams for Education](https://www.microsoft.com/en-us/education/products/teams)
  * [Microsoft 365 Education](https://www.microsoft.com/en-us/education/products/microsoft-365)
  * [How to buy for your school](https://www.microsoft.com/education/how-to-buy)
  * [Educator training and development](https://education.microsoft.com/)
  * [Deals for students and parents](https://www.microsoft.com/en-us/store/b/education)
  * [AI for education](https://www.microsoft.com/en-us/education/ai-in-education)



Business

  * [Microsoft Cloud](https://www.microsoft.com/en-us/microsoft-cloud)
  * [Microsoft Security](https://www.microsoft.com/en-us/security)
  * [Dynamics 365](https://www.microsoft.com/en-us/dynamics-365)
  * [Microsoft 365](https://www.microsoft.com/en-us/microsoft-365/business)
  * [Microsoft Power Platform](https://www.microsoft.com/en-us/power-platform)
  * [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software)
  * [Microsoft 365 Copilot](https://www.microsoft.com/en-us/microsoft-365-copilot?icid=DSM_Footer_Microsoft365Copilot)
  * [Small Business](https://www.microsoft.com/en-us/store/b/business?icid=CNavBusinessStore)



Developer & IT

  * [Azure](https://azure.microsoft.com/en-us/)
  * [Microsoft Developer](https://developer.microsoft.com/en-us/)
  * [Microsoft Learn](https://learn.microsoft.com/)
  * [Support for AI marketplace apps](https://www.microsoft.com/software-development-companies/offers-benefits/isv-success?icid=DSM_Footer_SupportAIMarketplace&ocid=cmm3atxvn98)
  * [Microsoft Tech Community](https://techcommunity.microsoft.com/)
  * [Microsoft Marketplace](https://marketplace.microsoft.com?icid=DSM_Footer_Marketplace&ocid=cmm3atxvn98)
  * [Marketplace Rewards](https://www.microsoft.com/software-development-companies/offers-benefits/marketplace-rewards?icid=DSM_Footer_MarketplaceRewards&ocid=cmm3atxvn98)
  * [Visual Studio](https://visualstudio.microsoft.com/)



Company

  * [Careers](https://careers.microsoft.com/)
  * [About Microsoft](https://www.microsoft.com/about)
  * [Company news](https://news.microsoft.com/source/?icid=DSM_Footer_Company_CompanyNews)
  * [Privacy at Microsoft](https://www.microsoft.com/en-us/privacy?icid=DSM_Footer_Company_Privacy)
  * [Investors](https://www.microsoft.com/investor/default.aspx)
  * [Diversity and inclusion](https://www.microsoft.com/en-us/diversity/default?icid=DSM_Footer_Company_Diversity)
  * [Accessibility](https://www.microsoft.com/en-us/accessibility)
  * [Sustainability](https://www.microsoft.com/en-us/sustainability/)



[ Your Privacy Choices Opt-Out Icon Your Privacy Choices ](https://aka.ms/yourcaliforniaprivacychoices) [ Your Privacy Choices Opt-Out Icon Your Privacy Choices ](https://aka.ms/yourcaliforniaprivacychoices) [ Consumer Health Privacy ](https://go.microsoft.com/fwlink/?linkid=2259814)

  * [Sitemap](https://www.microsoft.com/en-us/sitemap1.aspx)
  * [Contact Microsoft](https://support.microsoft.com/contactus)
  * [Privacy ](https://go.microsoft.com/fwlink/?LinkId=521839)
  * Manage cookies
  * [Terms of use](https://go.microsoft.com/fwlink/?LinkID=206977)
  * [Trademarks](https://go.microsoft.com/fwlink/?linkid=2196228)
  * [Safety & eco](https://go.microsoft.com/fwlink/?linkid=2196227)
  * [Recycling](https://www.microsoft.com/en-us/legal/compliance/recycling)
  * [About our ads](https://choice.microsoft.com)
  * (C) Microsoft 2025


