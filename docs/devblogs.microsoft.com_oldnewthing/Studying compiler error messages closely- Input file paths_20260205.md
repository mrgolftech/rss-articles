# Studying compiler error messages closely: Input file paths

**来源:** https://devblogs.microsoft.com_oldnewthing
**链接:** https://devblogs.microsoft.com/oldnewthing/20260202-00/?p=112027
**日期:** Mon, 02 Feb 2026 15:00:00 +0000

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
  * Studying compiler error messages closely: Input file paths



February 2nd, 2026

![like](https://devblogs.microsoft.com/oldnewthing/wp-content/themes/devblogs-evo/images/emojis/like.svg)1 reaction

# Studying compiler error messages closely: Input file paths

![Raymond Chen](https://devblogs.microsoft.com/oldnewthing/wp-content/uploads/sites/38/2019/02/RaymondChen_5in-150x150.jpg)

[Raymond Chen](https://devblogs.microsoft.com/oldnewthing/author/oldnewthing)

## 


[Show more](javascript:)

A colleague was working in a project that used a number of data files to configure how the program worked. They wanted one portion of the configuration file to be included only if a particular build flag was set. Let's say that the configuration file is `C:\repos\contoso\config\Contoso.config`.
    
    
    <providers>
        <!-- Widget version should be 1.0, or 2.0 if the useV2Widgets build flag is set -->
        <provider name="Widget" version="1.0"/>
    
        <!-- Gadget is needed only if the useV2Widgets build flag is set -->
        <provider name="Gadget" version="1.0"/>
    
        <!-- other providers that are used regardless of the build flags -->
    </providers>
    

They were adding a build flag to convert the code base to use 2.0 widgets, but they wanted the default to be 1.0; only people who build with the special build flag should get 2.0 widgets. It so happens that 2.0 widgets depend on gadgets, so they also wanted to add a gadget provider, but again only conditionally based on the build flag.

The configuration file itself doesn't support conditionals. How can they get a configuration file to support conditionals when the file format does not support conditionals?

I suggested that they [ use a preprocessor](https://devblogs.microsoft.com/oldnewthing/20090724-00/?p=17373 "If you wished a language supported the preprocessor, you know, you can fix that") to take the marked-up configuration file and produce a filtered output file, which becomes the _actual_ configuration file. Upon closer investigation, it appeared that they were not the first project to need conditionals in their configuration file, and another team had already written a generic XML preprocessor that supports conditional elements based on build flags, and that other team even included instructions on their project wiki on how to include a preprocessor pass to their build configuration. The updated configuration file looks something like this:
    
    
    <providers>
        <provider name="Widget" version="1.0" condition="!useV2Widgets"/>
        <provider name="Widget" version="2.0" condition="useV2Widgets"/>
        <provider name="Gadget" version="1.0" condition="useV2Widgets"/>
    </providers>
    

However, after following the instructions on the wiki to update the configuration file to use the `condition` attribute, and update the build process to send the file through the "conditional build flags" preprocessor, the was still a build error:
    
    
    Validation failure: C:\repos\contoso\config\Contoso.config(2): Invalid attribute 'condition'
    

The configuration validator was upset at the `condition` attribute, but when they compared their project to other projects that used the configuration preprocessor, those other projects used the `condition` attribute just fine.

Look carefully at the error message. In particular, look at the path to the file that the validator is complaining about.

The validator is complaining about the original _unprocessed_ file.

They went to the effort of sending the unprocessed file through the conditional build flags preprocessor to produce a processed file that has the correct provider list based on the build flags. But they forgot to use the results of that hard work: They were still using the old unprocessed file. It's like taking a photograph, doing digital touch-ups, but then uploading the original version instead of the touched-up version.

The fix was to update the project so that it consumed the processed file instead of the raw file.¹

**Bonus chatter** : To avoid this type of confusion, it is common to change the extension of the unprocessed file to emphasize that it needs to be preprocessed. That way, when you see an error in `Contoso.config`, you don't have to spend the effort to figure out _which_ `Contoso.config` the error is about.

In this case, they could rename the unprocessed file to `Contoso.preconfig` and have the processed output be `Contoso.config`. I choose this pattern because the validator may require that the file extension be `.config`.

Another pattern would be to call the unprocessed version `Contoso-raw.config` and the processed version `Contoso.config`.

If you don't want to rename an existing file (say because you are worried about merge errors if your change collides with others who are also modifying that file), you could leave the unprocessed file as `Contoso.config` and call the processed file `Contoso-final.config`.²

¹ The instructions on the wiki says "In your project file, change references from `yourfile.ext` to `$(OutputDirectory)\yourfile.ext`' But in this case, the file was being used not by the project file but by a separate configuration tool. The team was too focused on reading the literal instructions without trying to understand why the instructions were saying the things that they did. In this case, the instructions were focused on consumption from the project file, since that was the use case of the team that wrote the tool originally. But if you understand what the steps are trying to accomplish, you should realize that the intention is to update the references to the old `yourfile.ext` in _every location_ you want to consume the postprocessed version.³

² I chose the suffix `-final` as a joking reference to the pattern of seeing files named `Document-Final-Final-Final 2-USETHISONE.docx`.

³ I took the liberty of updating the wiki to clarify that you need to update _all_ references to `yourfile.ext`. The references usually come from the project file, but they could be in other places, too, such as a call to `makepri.exe`.

[ 1](https://devblogs.microsoft.com/oldnewthing/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Foldnewthing%2F20260202-00%2F%3Fp%3D112027 "Sign in to react")

  *   *   *   *   *   * 


5

0 

  * [ ![Facebook](https://devblogs.microsoft.com/oldnewthing/wp-content/themes/devblogs-evo/images/social-icons/facebook.svg) Share on Facebook ](https://www.facebook.com/sharer/sharer.php?u=https://devblogs.microsoft.com/oldnewthing/20260202-00/?p=112027 "Share on Facebook")
  * [ Share on X ](https://twitter.com/intent/tweet?url=https://devblogs.microsoft.com/oldnewthing/20260202-00/?p=112027&text=Studying compiler error messages closely: Input file paths "Share on X")
  * [ ![LinkedIn](https://devblogs.microsoft.com/oldnewthing/wp-content/themes/devblogs-evo/images/social-icons/linkedin.svg) Share on Linkedin ](https://www.linkedin.com/shareArticle?mini=true&url=https://devblogs.microsoft.com/oldnewthing/20260202-00/?p=112027 "Share on LinkedIn")



Category

[Old New Thing](https://devblogs.microsoft.com/oldnewthing/category/oldnewthing)

Topics

[Code](https://devblogs.microsoft.com/oldnewthing/tag/code)

Share

  * [ ](https://www.facebook.com/sharer/sharer.php?u=https://devblogs.microsoft.com/oldnewthing/20260202-00/?p=112027)
  * [ ](https://twitter.com/intent/tweet?url=https://devblogs.microsoft.com/oldnewthing/20260202-00/?p=112027&text=Studying compiler error messages closely: Input file paths)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https://devblogs.microsoft.com/oldnewthing/20260202-00/?p=112027)



## Author

![Raymond Chen](https://devblogs.microsoft.com/oldnewthing/wp-content/uploads/sites/38/2019/02/RaymondChen_5in-150x150.jpg)

[Raymond Chen](https://devblogs.microsoft.com/oldnewthing/author/oldnewthing)

Raymond has been involved in the evolution of Windows for more than 30 years. In 2003, he began a Web site known as The Old New Thing which has grown in popularity far beyond his wildest imagination, a development which still gives him the heebie-jeebies. The Web site spawned a book, coincidentally also titled The Old New Thing (Addison Wesley 2007). He occasionally appears on the Windows Dev Docs Twitter account to tell stories which convey no useful information.

##  5 comments 

Join the discussion.

### [Leave a comment](javascript:void\(0\) "Leave a comment")[Cancel reply](/oldnewthing/20260202-00/?p=112027#respond)

[Sign in](https://devblogs.microsoft.com/oldnewthing/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Foldnewthing%2F20260202-00%2F%3Fp%3D112027%23comments)

[Code of Conduct](https://aka.ms/msftqacodeconduct)

Sort by :

Newest

[Newest](javascript:void\(0\)) [Popular](javascript:void\(0\)) [Oldest](javascript:void\(0\))

  * ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAAAyAQMAAACQ++z9AAAAA1BMVEXW1taWrGEgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAD0lEQVQokWNgGAWjYGgCAAK8AAGBAoNpAAAAAElFTkSuQmCC)

raykoopa  February 2, 2026  * Edited 0

Collapse this comment Copy link

@Henry Skoglund: That just always reminds me of a Five Young Cannibals album.

[Log in to Vote or Reply](https://devblogs.microsoft.com/oldnewthing/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Foldnewthing%2F20260202-00%2F%3Fp%3D112027%23comments)

    * ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAAAyAQMAAACQ++z9AAAAA1BMVEXW1taWrGEgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAD0lEQVQokWNgGAWjYGgCAAK8AAGBAoNpAAAAAElFTkSuQmCC)

Henry Skoglund  February 2, 2026  0

Collapse this comment Copy link

Yeah, the album is from 1989, when OS/2 was king of the hill (before Windows 3.0 in 1990.)  
Maybe the devs listened to that music, or the album was produced/mixed using OS/2 (unlikely 🙂  
P.S. It's "Fine Young Cannibals" (consisting of 3 people/cannibals).

[Log in to Vote or Reply](https://devblogs.microsoft.com/oldnewthing/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Foldnewthing%2F20260202-00%2F%3Fp%3D112027%23comments)

  * ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAAAyAQMAAACQ++z9AAAAA1BMVEXW1taWrGEgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAD0lEQVQokWNgGAWjYGgCAAK8AAGBAoNpAAAAAElFTkSuQmCC)

Michael Taylor  3 days ago  1

Collapse this comment Copy link

I'm assuming it is a copy/paste issue with your code but when I read the error message I saw that it was having an issue with the attribute `conditions`. But in the earlier code sample the attribute was called `condition`.

[Log in to Vote or Reply](https://devblogs.microsoft.com/oldnewthing/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Foldnewthing%2F20260202-00%2F%3Fp%3D112027%23comments)

    * ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAACWAQMAAAAGz+OhAAAAA1BMVEXW1taWrGEgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAGklEQVRIie3BMQEAAADCoPVPbQ0PoAAAgHcDC7gAAaFsh3EAAAAASUVORK5CYII=)

[Raymond Chen![Microsoft employee](https://devblogs.microsoft.com/oldnewthing/wp-content/plugins/devblogs-comments-evo/admin/images/MicrosoftLogo_50x50.png) Author](https://devblogs.microsoft.com/oldnewthing/author/oldnewthing "Raymond Chen") 3 days ago  1

Collapse this comment Copy link

Thanks. I knew I had that error and made a mental note to fix it, but when I went back, I couldn't find it. But now you found it for me, so I fixed it.

[Log in to Vote or Reply](https://devblogs.microsoft.com/oldnewthing/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Foldnewthing%2F20260202-00%2F%3Fp%3D112027%23comments)

  * ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAAAyAQMAAACQ++z9AAAAA1BMVEXW1taWrGEgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAD0lEQVQokWNgGAWjYGgCAAK8AAGBAoNpAAAAAElFTkSuQmCC)

Henry Skoglund  3 days ago  1

Collapse this comment Copy link

I picked up the terms "raw" and "cooked" from some OS/2 programming, and used them since for naming stuff before they're "being munged/processed" to after.

[Log in to Vote or Reply](https://devblogs.microsoft.com/oldnewthing/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Foldnewthing%2F20260202-00%2F%3Fp%3D112027%23comments)




## Read next

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

[Sign in](https://devblogs.microsoft.com/oldnewthing/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Foldnewthing%2F20260202-00%2F%3Fp%3D112027)

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


