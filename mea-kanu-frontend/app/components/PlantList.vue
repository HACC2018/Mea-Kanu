<template>
    <Page class="page">
        <ActionBar class="action-bar">
            <Label class="action-bar-title" text="Mea Kanu" horizontalAlignment="center"/>
            <ActionItem @tap="uploadPicture" android.systemIcon="ic_menu_upload" android.position="actionBar"/>
            <NavigationButton text="Go Back" android.systemIcon="ic_menu_camera" @tap="openCam"/>
            <!--<ActivityIndicator :busy="isBusy" class="activity-indicator" color="orange"/>-->
        </ActionBar>

        <!--<Stacklayout>-->
            <!--<Button text="lambda test" @tap="lambdaExample" class="btn btn-primary"></Button>-->
        <!--</Stacklayout>-->


        <RadListView ref="listView" for="(plant, index) in plantList" @itemTap="onItemTap" class="list-group">
            <ListViewLinearLayout v-tkListViewLayout scrollDirection="vertical"/>
            <v-template>

                <GridLayout rows="*, *, *" columns="*, *" class="list-group-item-content">
                    <Label :text="plant.commonName"
                           class="text-primary list-group-item-text font-weight-bold"/>

                    <Label row="1" class="hr-dark m-t-5 m-b-5" colSpan="2"/>

                    <Image row="2" :src="plant.picture" stretch="aspectFill" height="120" class="m-r-20"
                           loadMode="async"/>

                    <StackLayout row="2" col="1" verticalAlignment="center" class="list-group-item-text">
                        <Label class="p-b-10">
                            <FormattedString>
                                <Span text.decode="&#xf12a;   " class="fa text-primary"/>
                                <Span :text="plant.conservationStatus"/>
                            </FormattedString>
                        </Label>

                        <Label class="p-b-10">
                            <FormattedString>
                                <Span text.decode="&#xf0c3;   " class="fa text-primary"/>
                                <Span :text="plant.species"/>
                            </FormattedString>
                        </Label>

                        <Label class="p-b-10">
                            <FormattedString>
                                <Span text.decode="&#xf0ac;   " class="fa text-primary"/>
                                <Span :text="plant.hawaiianName"/>
                            </FormattedString>
                        </Label>
                    </StackLayout>
                </GridLayout>
            </v-template>

        </RadListView>
    </Page>
</template>

<script>

    import * as camera from "nativescript-camera";
    import axios from 'axios';
    import * as http from "http";
    //import * as axios from "axios/dist/axios";
    import * as imageSource from "tns-core-modules/image-source";
    import PlantDetails from "./PlantDetails";
    import PlantResults from './PlantResults';

    var imagepicker = require("nativescript-imagepicker");
    const enums = require("ui/enums");
    export default {

        data() {
            return {
                // pictureFromCamera: null,
                // textPicture: "Take a Picture",
                isBusy: false,
                picture: null,
                imagePicker: [],
                pictureBase64String: '',
                pictureAxios: null,
                percentages: [],
                plantList:
                    [{
                        class: 0,
                        picture: "~/images/abutilon_menziesii.jpg",
                        commonName: "Red abutilon",
                        conservationStatus: "Critically Endangered",
                        description: "Abutilon menziesii, known as Kooloaula in Hawaiian, is an endangered species of flowering shrub in the mallow family, Malvaceae, that is endemic to Hawaii. It inhabits dry forests on the islands of Lanai, Maui, Oahu and Hawaii.",
                        hawaiianName: "Kooloaula",
                        species: "Abutilon menziesii",
                        status: "Endemic",
                        story: "Not Available",
                        uses: "This is a definite must-have for any plant collector or weekend warrior gardener. Ko’oloa’ula thrives in full sun and dry areas. Watering is OK, but it is best to soak the ground and avoid watering again until the soil dries completely."
                    }, {
                        class: 1,
                        picture: "~/images/achyranthes_splendens.jpg",
                        commonName: "Round chaff flower",
                        conservationStatus: "Vulnerable",
                        description: "Achyranthes splendens is a species of flowering plant in the pigweed family, Amaranthaceae, that is endemic to Hawai'i. Its natural habitats are dry forests, low shrublands, and sandy shores. It is threatened by habitat loss.",
                        hawaiianName: "Ahinahina",
                        species: "Achyranthes splendens",
                        status: "Endemic",
                        story: "Not Available",
                        uses: "The spikes and new leaves of this plant are used in Wili and Haku Lei."
                    }, {
                        class: 2,
                        picture: "~/images/bonamia_menziesii.jpg", commonName: "Hawaii lady's nightcap",
                        conservationStatus: "Endangered",
                        description: "Bonamia menziesii, commonly known as Hawai'i lady's nightcap, is a species of flowering plant in the morning glory family, Convolvulaceae, that is endemic to Hawaii. It is a vine or twisting liana with branches that can reach 10 m in length.",
                        hawaiianName: "Puuwaawaa",
                        species: "Bonamia menziesii",
                        status: "Endemic",
                        story: "Not Available",
                        uses: "This is an excellent vine for chain link fencing or over larger shrubs. The plants will twine around themselves if they do not have something else to."
                    }, {
                        class: 3,
                        picture: "~/images/cyperus_trachysanthos.jpg", commonName: "Sticky flatsedge",
                        conservationStatus: "Endangered",
                        description: "Cyperus trachysanthos is a rare species of sedge known by the common names pu'uka'a and sticky flatsedge. It is endemic to Hawaii, where it is known from Kauai and Oahu. It was known from Niihau, Molokai and Lanai, but it has been extirpated from these islands.",
                        hawaiianName: "Puukaa",
                        species: "Cyperus trachysanthos",
                        status: "Endemic",
                        story: "One of the few remnant populations of this plant was at a place called Kealakipapa more commonly known as Allen Davis or the place where everyone parks to hike up to the Makapu’u lighthouse, the reason I say was is because recently this area fell victim to a brush fire that burned approximately 50 acres of land including the vernal pond in which this plant lived and numerous other native plants. Hopefully this population has not become extinct.",
                        uses: "This plant can be placed in or around water features as well as in the soil as long as it is watered regularly. Pruning of dead leaves keeps this plant looking full and beautiful. It looks great when planted along side rock features or as an accent combined with plants like groundcovers or other plants from which it can “burst” up out of. Pu’uka’a can also be added to dry floral arrangements to add some real flair. Few pests bother this plant but occasionally you may find some aphids on the new shoots, these can be taken care of simply by running your fingers up the leaf. Be careful though because the leaf blades are so slender that once they are bent and creased they won’t perk back up."
                    }, {
                        class: 4,
                        picture: "~/images/gouania_hillebrandii.jpg", commonName: "Hairy-fruit chewstick",
                        conservationStatus: "Endangered",
                        description: "Gouania hillebrandii is an endangered species of Gouania that is endemic to Hawaii. It formerly could be found on Maui, Moloka'i, Lana'i and Kaho'olawe, but is today restricted to western Maui near Lahaina. It inhabits dry forests at elevations of 244 - 518 m.",
                        hawaiianName: "Not Available",
                        species: "Gouania hillebrandii",
                        status: "Endemic",
                        story: "Other native species in the same family are the indigenous shrub ʻānapanapa (Colubrina asiatica), and two endemic trees, both called kauila or kawila, Alphitonia ponderosa and Colubrina oppositifolia.",
                        uses: "The hairy-fruit chewstick (Gouania hillebrandii) is an attractive native shrub with great potential for the landscape if it becomes readily available."
                    }, {
                        class: 5,
                        picture: "~/images/hibiscus_brackenridgei.jpg", commonName: "Mao hau hele",
                        conservationStatus: "Endangered",
                        description: "Hawaiian hibiscus are seven species of hibiscus regarded as native to Hawaii. The yellow hibiscus is Hawaii's state flower.",
                        hawaiianName: "Mao hau hele",
                        species: "Hibiscus brackenridgei",
                        status: "Endemic",
                        story: "The name of this plant- ma’o hau hele literally means the “traveling green hau”. It is probable that it got this name because after the plant gets to be about 3-5 years old it will become top heavy and either lean over or fall over and sprout new roots where the leaning branches touch the ground. Sometimes the old portion of the plant will die and the newly sprouted roots from the leaning branches will make the same plant thrive in a new spot a few feet over from its original location. Over time if the plant continues to flop over and sprout new roots it can move quite some distance. A friend of mine Lorin Gill recalls a particular ma’o hau hele traveling over 20 ft in about 15 years! In 1988 the State of Hawai’i changed the state flower from the native red hibiscus (Hibiscus kokio) to this one. It should be made clear that this is the only species of yellow hibiscus that can be called our state flower, all other yellow hibiscus are not.",
                        uses: "Sometimes the ovaries/bases of the flower were used as an alternative to hau sap as a mild laxative (Krauss 1993:102)"
                    }, {
                        class: 6,
                        picture: "~/images/panicum_fauriei.jpg", commonName: "Faurie's panicgrass",
                        conservationStatus: "Endangered",
                        description: "Panicum fauriei is a species of grass known by the common name Faurie's panicgrass. It is endemic to Hawaii. There are at least three varieties of this grass species. One, var. carteri, Carter's panicgrass is federally listed as an endangered species of the United States.",
                        hawaiianName: "Not Available",
                        species: "Panicum fauriei",
                        status: "Endemic",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 7,
                        picture: "~/images/portulaca_villosa.jpg", commonName: "Hairy purslane",
                        conservationStatus: "At-risk",
                        description: "Portulaca oleracea is an annual succulent in the family Portulacaceae, which may reach 40 cm in height. Approximately forty cultivars are currently grown.",
                        hawaiianName: "Ihi",
                        species: "Portulaca villosa",
                        status: "Endemic",
                        story: "Not Available",
                        uses: "An excellent bedding or accent plant with very good drainage. [Rick Barboza, Hui Kū Maoli Ola] These are great potted plants for the often harsh conditions on full sun and windy porches or lānais. If kept in containers, use a 4 to 6 inch cement, terra cotta, or unglazed ceramic pots which are preferred over plastic ones. These types of potting containers tend to breath better and allow potting mix to dry out quicker, essential for the health of these xeric plants. Too, the weight of the pots will help these succulents from toppling over in windy conditions and as they grow larger in the pots. Use a very dry potting mix (i.e. cactus mix) with perfect drainage.This species has proven to be a great indoor plant, but only if used in a very sunny window planted excellent drainage. Plant them in a perfect drainage media such as for cactus, that is with mostly free draining potting materials such as a 4:1 ratio of 4 parts perlite and/or black cinder to 1 part good potting \"soil\" (e.g. Sunshine #4). But as mentioned, cement or terra cotte pots are best. Keep watering very minimal. [David Eickhoff, Native Plants "
                    }, {
                        class: 8,
                        picture: "~/images/scaevola_coriacea.jpg", commonName: "Dwarf naupaka",
                        conservationStatus: "Endangered",
                        description: "Scaevola coriacea, the dwarf naupaka, is a species of flowering plant in the Goodenia family, Goodeniaceae, that is endemic to Hawaii.",
                        hawaiianName: "Naupaka papa",
                        species: "Scaevola coriacea",
                        status: "Endemic",
                        story: "It is believed that all nine species of naupaka (two coastal and seven mountain) came from three separate colonizations: one for the common beach naupaka, which is indigenous; another for ‘ohe naupaka (S. glabra), a spectacular mountain species with large tubular yellow flowers not typical of naupaka; and finally a third colonization covering all the rest of the species, including six mountain species and this coastal one.",
                        uses: "Purplish black dye made from fruit (Krauss 1993:66)"
                    }, {
                        class: 9,
                        picture: "~/images/sesbania_tomentosa.jpg", commonName: "Oahu riverhemp",
                        conservationStatus: "Endangered",
                        description: "Sesbania tomentosa, commonly known as Oahu riverhemp and Ohai, is an endangered species of flowering plant in the pea family, Fabaceae, that is endemic to the main Hawaiian Islands as well as Nihoa and Necker Island.",
                        hawaiianName: "Ohai",
                        species: "Sesbania tomentosa",
                        status: "Endemic",
                        story: "`Ōlelo Noeau: [I] Ka wahine hele la o Kaiona, alualu wai li‘ulä o ke kaha pua ‘ohai. The woman, Kaiona, who travels in the sunshine pursuing the mirage of the place where the ‘ohai blossoms grow. Kaiona was a goddess of Ka‘ala and the Wai‘anae Mountains. She was a kind person who helped anyone who lost his way in the mountains by sending a bird, an ‘iwa, to guide the lost one out of the forest. In modern times Princess Bernice Pauahi Bishop was compared to Kaiona in songs. [II] Ke kaha ‘ohai o Kaiona. Kaiona's place where the ‘ohai grows. Kaiona is a benevolent goddess whose home is Mt. Ka‘ala and vicinity. The ‘ohai grew in profusion there, Princess Bernice Pauahi Bishop was compared to this goddess in songs. [III] ‘Ohai o Papiohuli. The ‘ohai of Papiohuli. At Papiohuli, Mana, Kaua‘i, grew ‘ohai trees that bore red or whitish blossoms. These trees grew in profusion in the olden days but are now rare. The blossoms made beautiful lei.",
                        uses: "`Ōlelo Noeau: ‘Awapuhi lau pala wale. Ginger leaves yellow quickly. Said of a weakling who withers easily, or of anything that passes too soon."
                    }, {
                        class: 10,
                        picture: "~/images/acacia_confusa.jpg", commonName: "Small Philippine acacia",
                        conservationStatus: "Low risk",
                        description: "Some common names for it are acacia petit feuille, small Philippine acacia, Formosa acacia (Taiwan acacia) and Formosan koa. It grows to a height of 50 ft. The tree has become very common in many tropical Pacific areas, including Hawaii, where the species is considered invasive.",
                        hawaiianName: "Not Available",
                        species: "Acacia confusa",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 11,
                        picture: "~/images/acalypha_hispida.jpg", commonName: "Philippines medusa",
                        conservationStatus: "Low risk",
                        description: "Commonly called chenille plant and red-hot cat's tail is a beautiful flowering plant that has a long bloom period. This plant is also known as the Philippines Medusa, pokok ekor kucing in Malay, Rabo de Gato in Portuguese, and shibjhul in Bengali. Acalypha hispida is cultivated as a house plant because of its attractiveness and brilliantly colored, furry flowers.",
                        hawaiianName: "Not Available",
                        species: "Acalypha hispida",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 12,
                        picture: "~/images/aloe_vera.jpg", commonName: "Aloe vera",
                        conservationStatus: "Low risk",
                        description: "Common names include Chinese Aloe, Indian Aloe, True Aloe, Barbados Aloe, Burn Aloe, First Aid Plant. An evergreen perennial, it originates from the Arabian Peninsula but grows wild in tropical climates around the world and is cultivated for agricultural and medicinal uses. The species is also used for decorative purposes and grows successfully indoors as a potted plant.",
                        hawaiianName: "Not Available",
                        species: "Aloe vera",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Remedy for Irritable bowel syndrome.  Cut skin and spikes off, filet,"
                    }, {
                        class: 13,
                        picture: "~/images/alpinia_purpurata.jpg", commonName: "Red ginger",
                        conservationStatus: "Low-risk",
                        description: "The red ginger, also called ostrich plume and pink cone ginger, is a species with showy flowers on long brightly colored red bracts. It prefers partial shade and moist humid conditions, although it can tolerate full sun in some climates. It tends to like to be well watered and not left to dry out. Ginger can also be grown as a houseplant and its cut flowers can be used in arrangements.",
                        hawaiianName: "Awapuhi",
                        species: "Alpinia purpurata",
                        status: "Invasive",
                        story: "`Ōlelo Noeau: ‘Awapuhi lau pala wale. Ginger leaves yellow quickly. Said of a weakling who withers easily, or of anything that passes too soon.",
                        uses: "‘Awapuhi is used as a compress to apply to sore spots, bruises and cuts; also for headaches, toothache, ringworm/other skin disease, achy joints/sprains, stomach-ache (it is said to have anti-inflammatory properties). Ashes from burnt leaves, combined with a mixture of ashes of ‘ohe lau li‘i (small-leaved bamboo, Schizostachyum glaucifolium) and kukui nut sap (Aleurites moluccana), and ‘awapuhi tuber sap, provided a remedy for cuts and bruised skin. Underground stems were mashed with salt and rubbed on the head to treat headaches (Abbott 1992:102; Chun 1994:61–64).  Sometimes used on kuahu (hula altars) (Pukui 1942). Fragrant, sudsy fluid squeezed out of plant for use as shampoo, the powdered rhizome for scenting kapa, and leaves used to flavor meat (Wagner et al. 1990:1624)."
                    }, {
                        class: 14,
                        picture: "~/images/anthurium_andreanum.jpg", commonName: "Tailflower",
                        conservationStatus: "Low risk",
                        description: "Common names for this species include tailflower, flamingo flower, and laceleaf. Its name comes from the Greek words anthos, meaning flower, and oura, meaning a tail. It is a monocotyledonous perennial, preferring warm, shady and humid climates, such as tropical rainforests. Its most characteristic feature as an ornamental is its brightly colored spathe leaf, and the protruding inflorescence called the spadix.",
                        hawaiianName: "Not Available",
                        species: "Anthurium andreanum",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 15,
                        picture: "~/images/bauhinia_variegata.jpg", commonName: "Orchid tree",
                        conservationStatus: "Low-risk",
                        description: "Common names include orchid tree, camel's foot tree, kachnar, and mountain-ebony. This is a very popular ornamental tree in subtropical and tropical climates. It is a small to medium-sized tree growing up to 39 ft tall, deciduous in the dry season. This is a very popular ornamental tree in subtropical and tropical climates, grown for its scented flowers and also used as food item in South Asian cuisine.",
                        hawaiianName: "Not Available",
                        species: "Bauhinia variegata",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 16,
                        picture: "~/images/bixa_orellana.jpg", commonName: "Lipstick tree",
                        conservationStatus: "Low-risk",
                        description: "Also known as Achiote, this species is a shrub or small tree originating from the tropical region of the Americas. North, Central, and South American natives originally used the seeds to make red body paint and lipstick, as well as a spice. For this reason, the achiote is sometimes called the lipstick tree.",
                        hawaiianName: "Not Available",
                        species: "Bixa orellana",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 17,
                        picture: "~/images/blighia_sapida.jpg", commonName: "Ackee",
                        conservationStatus: "Low-risk",
                        description: "The ackee, also known as achee, ackee apple or ayee is a fruit, which is the member of the Sapindaceae (soapberry family). Ackee is an evergreen tree that grows about 33 ft tall, with a short trunk and a dense crown. Although native to West Africa, the use of ackee in food is especially prominent in Jamaican cuisine. Ackee is the national fruit of Jamaica, and ackee and saltfish is the national dish.",
                        hawaiianName: "Not Available",
                        species: "Blighia sapida",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 18,
                        picture: "~/images/bombax_glabra.jpg", commonName: "French peanut",
                        conservationStatus: "Low-risk",
                        description: "Also known as Malabar Chestnut, Pachira aquatica, Guiana chestnut, provision tree, saba nut, Monguba, Pumpo and is commercially sold under the names money tree and money plant. This tree is sometimes sold with a braided trunk and is commonly grown as a houseplant.",
                        hawaiianName: "Not Available",
                        species: "Bombax glabra",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 19,
                        picture: "~/images/bougainvillea_sp.jpg", commonName: "Great Bougainvillea",
                        conservationStatus: "Low-risk",
                        description: "Also known as great bougainvillea, is a species of flowering plant. This plant is also widely grown as an ornamental plant. It grows as a woody vine or shrub, reaching up to 40 feet with heart-shaped leaves and thorny, pubescent stems. The flowers are generally small, white, and inconspicuous, highlighted by several brightly colored modified leaves called bracts.",
                        hawaiianName: "Not Available",
                        species: "Bougainvillea sp",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 20,
                        picture: "~/images/brugmansia_x_candida.jpg", commonName: "Angel's trumpet",
                        conservationStatus: "Low-risk",
                        description: "Their large, fragrant flowers give them their common name of angel's trumpets. They are woody trees or shrubs, with pendulous flowers, and have no spines on their fruit. They are large shrubs or small trees, with semi-woody, often many-branched trunks. They can reach heights up to 36 ft. The leaves are alternately arranged along the stems with an entire or coarsely toothed margin, and are often covered with fine hairs. ",
                        hawaiianName: "Not Available",
                        species: "Brugmansia x candida",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 21,
                        picture: "~/images/caesalpinia_pulcherrima.jpg", commonName: "Peacock flower",
                        conservationStatus: "Low-risk",
                        description: "Common names for this species include poinciana, peacock flower, red bird of paradise, dwarf poinciana, flos pavonis, flamboyant-de-jardin and ohai ali'i in Hawaiian. It is a shrub growing to 10 ft tall. In climates with few to no frosts, this plant will grow larger and is semievergreen. Grown in climates with light to moderate freezing, plant will die back to the ground depending on cold, but will rebound in mid- to late spring.",
                        hawaiianName: "Ohai alii",
                        species: "Caesalpinia pulcherrima",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 22,
                        picture: "~/images/calotropis_gigantea.jpg", commonName: "Booc booc",
                        conservationStatus: "Low-risk",
                        description: "Commonly called crown flower or giant milkweed, is a large shrub or small tree cultivated in tropical areas around the world. It is a large shrub growing to 13 ft tall. It has clusters of waxy flowers that are either white or lavender in colour. Each flower consists of five pointed petals and a small \"crown\" rising from the center which holds the stamens. ",
                        hawaiianName: "Not Available",
                        species: "Calotropis gigantea",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 23,
                        picture: "~/images/canna_indica.jpg", commonName: "Indian shot",
                        conservationStatus: "Low-risk",
                        description: "Commonly known as Indian shot, African arrowroot, edible canna, purple arrowroot, Sierra Leone arrowroot, is a plant species in the family Cannaceae. It has been cultivated by indigenous peoples of the Americas in tropical America for thousands of years. The place of the first domestication may have been the northern Andes, as may be true of other similar root crops.",
                        hawaiianName: "Not Available",
                        species: "Canna indica",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 24,
                        picture: "~/images/cardiospermum_grandiflorum.jpg", commonName: "Balloon vine",
                        conservationStatus: "Low-risk",
                        description: "Commonly known as balloon vine, heart pea or heart seed, is a species of climbing plant. It can grow over 33 ft long and it has small white flowers. It is also a weed of forests and forest margins, urban bushland, open woodlands, roadsides, fence-lines, disturbed sites, waste areas and neglected gardens in tropical, sub-tropical and warmer temperate regions.",
                        hawaiianName: "Not Available",
                        species: "Cardiospermum grandiflorum",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 25,
                        picture: "~/images/cascabela_thevetia.jpg", commonName: "Yellow oleander",
                        conservationStatus: "Low-risk",
                        description: "Commonly known as yellow oleander or lucky nut, these flowers are used for religious purpose especially in the worshipping of the God Shiva. It is an evergreen tropical shrub or small tree. Its leaves are willow-like, linear-lanceolate, and glossy green in color. They are covered in waxy coating to reduce water loss (typical of oleanders). Its stem is green turning silver/gray as it ages.",
                        hawaiianName: "Not Available",
                        species: "Cascabela thevetia",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 26,
                        picture: "~/images/cassia_bakeriana.jpg", commonName: "Wishing tree",
                        conservationStatus: "Low-risk",
                        description: "Commonly called pink shower or wishing tree, is a small flowering tree that typically matures up to 3 ft tall and as wide. This tree is now grown primarily as an ornamental in tropical and subtropical areas around the world. It is noted for producing a showy display of fragrant pink-purple flowers with yellow stamens.",
                        hawaiianName: "Not Available",
                        species: "Cassia bakeriana",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 27,
                        picture: "~/images/casuarina_equisetifolia.jpg", commonName: "Australian pine tree",
                        conservationStatus: "Low-risk",
                        description: "Common names include coast sheoak, beach casuarina, beach oak, whistling tree, horsetail she oak, horsetail beefwood, horsetail tree and agoho. Casuarina equisetifolia is an evergreen tree growing up to 115 ft tall. The foliage consists of slender bearing minute scale-leaves in whorls of 68. The flowers are produced in small catkin-like inflorescences.",
                        hawaiianName: "Not Available",
                        species: "Casuarina equisetifolia",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 28,
                        picture: "~/images/catharanthus_roseus.jpg", commonName: "Madigascar periwinkle",
                        conservationStatus: "Low-risk",
                        description: "Commonly known as the Madagascar periwinkle, rose periwinkle, or rosy periwinkle, is a species of flowering plant in the dogbane family Apocynaceae. In the wild, it is an endangered plant; the main cause of decline is habitat destruction by slash and burn agriculture. It is also however widely cultivated and is naturalised in subtropical and tropical areas of the world.",
                        hawaiianName: "Kihapai",
                        species: "Catharanthus roseus",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Use leaves, flowers, and soft part of plant, blend with 1 cup of water, strain, drink.  Cancer treatments, blood purifier."
                    }, {
                        class: 29,
                        picture: "~/images/cattleya_sp.jpg", commonName: "Cattleya orchid",
                        conservationStatus: "Low-risk",
                        description: "Common names are Cattleya Orchid and Corsage Orchid, like most orchids, priced for it's delicate and beautiful flowers. Epiphytic or terrestrial orchids with cylindrical rhizome from which the fleshy noodle-like roots grow. Pseudobulbs can be conical, spindle-shaped or cylindrical; with upright growth; one or two leaves growing from the top of them.",
                        hawaiianName: "Not Available",
                        species: "Cattleya sp",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 30,
                        picture: "~/images/chlorophytum_comosum.jpg", commonName: "Spider plant",
                        conservationStatus: "Low-risk",
                        description: "Often called spider plant but also known as airplane plant, St. Bernard's lily, spider ivy, ribbon plant, and hen and chickens is a species of perennial flowering plant. Chlorophytum comosum is a popular houseplant. The species with all-green leaves forms only a small proportion of plants sold. More common are two variegated cultivars: 'Vittatum' with a broad central white stripe and 'Variegatum' with white margins.",
                        hawaiianName: "Not Available",
                        species: "Chlorophytum comosum",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 31,
                        picture: "~/images/clerodendrum_quadriloculare.jpg", commonName: "Bronze-leaved clerodendrum",
                        conservationStatus: "Low-risk",
                        description: "Also called bronze-leaved clerodendrum, fire works, Philippine glorybower, shooting star or starburst bush, these plants produce flowers that can be a pest to eradicate. This is one of the tropic's most beautiful flowering shrubs. Large, dark-green and burgundy leaves are the backdrop for firework-resembling, pink and white flower clusters in late winter and early spring.",
                        hawaiianName: "Not Available",
                        species: "Clerodendrum quadriloculare",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 32,
                        picture: "~/images/clitoria_ternatea.jpg", commonName: "Asian pigeonwings",
                        conservationStatus: "Low-risk",
                        description: "Commonly known as Asian pigeonwings, bluebellvine, blue pea, butterfly pea, cordofan pea and Darwin pea, is a plant species belonging to the Fabaceae family. The flowers of this vine were imagined to have the shape of human female genitals, hence the Latin name of the genus \"Clitoria\", from \"clitoris\".",
                        hawaiianName: "Not Available",
                        species: "Clitoria ternatea",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 33,
                        picture: "~/images/cocos_nucifera.jpg", commonName: "Coconut palm",
                        conservationStatus: "Low-risk",
                        description: "The coconut palm, is a monocot perennial member of the Arecaceae family, cultivated in tropical areas worldwide for its fruit and fiber. Coconut palms are medium-sized, solitary herbaceous plants. Although treelike in form, their trunks are composed not of wood, but of fibrous, stout, overlapping stems, and may grow to 80 ft tall.",
                        hawaiianName: "Niu",
                        species: "Cocos nucifera",
                        status: "Indigenous",
                        story: "The gods Ku and Niuolahiki had kinolau or body forms as the coconut palm.",
                        uses: "Niu flesh, oil, leaf buds, and water were used in numerous medicines (see other plants). These include formulations for lepo pa‘a (constipation), ‘ea (thrush), pa‘ao‘ao, and the \"illness related to lolo\"; in addition, the leaf bud is made into a topical medicine for ‘eha moku kukonukonu and ‘eha ‘ulia wale (Chun 1998:41).  Niu (coconut) has many uses. The trunks used to make house posts, small canoes, hula drums, or food containers (Handy et al. 1972:173–175). Leaves (launiu) used to for baskets, thatch and for fans, known as some of the finest in Polynesia (Abbott 1993:61, 76; Summers 1990:75–78). Leaf sheaths used as food or fish-bait wrappers (Handy et al. 1972:173). Husk fibers also used for cordage to make nets or lashing, known as 'aha (Summers 1990:75); the cordage could be coarse or fine. The cordage can be made into supports for ‘umeke (bowls) or other round-based objects. Shell of fruit was used for eating utensils, such as spoons, bowls, plates, as well as ‘awa cups and strainers for ‘awa. An historic period piece in the Bishop Museum ethnology collection is in the form of a goblet. Niu shells also served for storage containers, lids, and knee drums or puniu (Krauss 1993:80–87; Handy et al. 1972:173–175); the fibers are made into a drum beater. A musical instrument, the hokiokio, can also be made from coconut shell. Small mortars and bull roarers (oeoe) are also made from the niu shell (Krauss 1993:45, 98–99). Niu water used as a drink, and flesh eaten raw or with poi (Handy et al. 1972:171. Some of the most familiar preparations of niu were not developed by ancient Hawaiians. Sometimes the niu \"shell\" used to make ‘uli‘uli (hula rattles) (Handy et al.1972:174). Oil from meat used on body and hair (Handy et al. 1972:174). In the Bishop Museum ethnology collection there are examples of the husk fibers used as kapa and a brush, and the leaves and husk as part of a game. The wood could be fashioned into an ‘ukeke, or musical bow. The mid-rib of the niu leaf is used as the \"skewer\" for a kukui nut torch (kali lukui) (Abbott 1992:77). Some recognize two forms introduced by Polynesians: niu hiwa (dark green husk and black shell) used ceremonially, medicinally and for cooking; niu lelo (reddish yellow husk and yellow shell), used for secular purposes, not for medicine or ceremonies (Handy et al. 1972:170; Summers 1990:75–78). In the Bishop Museum Ethnology collection there is an example of a post-contact bowl made from the trunk of the niu."
                    }, {
                        class: 34,
                        picture: "~/images/codiaeum_variegatum.jpg", commonName: "Garden croton",
                        conservationStatus: "Low-risk",
                        description: "Garden croton or variegated croton, this is a species of plant in the genus Codiaeum, which is a member of the family Euphorbiaceae. There are several hundred cultivars, selected and bred for their foliage. Depending on the cultivar, the leaves may be ovate to linear, entire to deeply lobed or crinkled, and variegated with green, white, purple, orange, yellow, red or pink.",
                        hawaiianName: "Not Available",
                        species: "Codiaeum variegatum",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 35,
                        picture: "~/images/couroupita_guianensis.jpg", commonName: "Cannonball tree",
                        conservationStatus: "Low-risk",
                        description: "Known by a variety of names including cannonball tree, it is cultivated in many tropical areas because of its beautiful, fragrant flowers and large fruits. Couroupita guianensis is a tree that reaches heights of up to 110 ft tall. It is planted as an ornamental for its showy, scented flowers, and as a botanical specimen for its interesting fruit.",
                        hawaiianName: "Not Available",
                        species: "Couroupita guianensis",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 36,
                        picture: "~/images/crescentia_cujete.jpg", commonName: "Calabash tree",
                        conservationStatus: "Low-risk",
                        description: "Commonly known as the Calabash Tree, is species of flowering plant with simple leaves, which are alternate or in fascicles on short shoots. The fruit, called Jcara, Bule, Tecomate, Guaje, Morro or Huacal in Mexico, is used to make small vessels for serving or drinking. ,The tree shares its common name with that of the vine calabash, or bottle gourd.",
                        hawaiianName: "Not Available",
                        species: "Crescentia cujete",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 37,
                        picture: "~/images/crinum_asiaticum.jpg", commonName: "Poison bulb",
                        conservationStatus: "Low-risk",
                        description: "Also known as poison bulb, giant crinum lily, grand crinum lily, or spider lily, this is a plant species widely planted in many warmer regions as an ornamental. It is a bulb-forming perennial producing an umbel of large, showy flowers that are prized by gardeners. All parts of the plant are, however, poisonous if ingested. Some reports indicate exposure to the sap may cause skin irritation.",
                        hawaiianName: "Not Available",
                        species: "Crinum asiaticum",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 38,
                        picture: "~/images/cupressus_sempervirens.jpg", commonName: "Mediterranean cypress",
                        conservationStatus: "Low-risk",
                        description: "Also known as Italian cypress, Tuscan cypress, Persian cypress, or pencil pine, this is a medium-sized coniferous evergreen tree to 115 ft tall. It is a medium-sized coniferous evergreen tree to 115 ft tall, with a conic crown with level branches and variably loosely hanging branchlets. It is very long-lived, with some trees reported to be over 1,000 years old.",
                        hawaiianName: "Not Available",
                        species: "Cupressus sempervirens",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 39,
                        picture: "~/images/cyperus_papyrus.jpg", commonName: "Paper reed",
                        conservationStatus: "Low-risk",
                        description: "Known as papyrus, papyrus sedge, paper reed, Indian matting plant, and Nile grass, this is a species of aquatic flowering plant belonging to the family Cyperaceae. It has a very long history of use by humans, it is the source of papyrus paper. Parts of the plant can be eaten, and the highly buoyant stems can be made into boats. It is now often cultivated as an ornamental plant.",
                        hawaiianName: "Not Available",
                        species: "Cyperus papyrus",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 40,
                        picture: "~/images/delonix_regia.jpg", commonName: "Royal poinciana",
                        conservationStatus: "Low-risk",
                        description: "The flame tree is a species of flowering plant in the bean family Fabaceae. It is noted for its fern-like leaves and flamboyant display of flowers. In many tropical parts of the world it is grown as an ornamental tree and in English it is given the name royal poinciana or flamboyant. It is also one of several trees known as \"flame tree\".",
                        hawaiianName: "Not Available",
                        species: "Delonix regia",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 41,
                        picture: "~/images/dendrobium_sp.jpg", commonName: "Dendrobium orchid",
                        conservationStatus: "Low-risk",
                        description: "These plants belong to a large and diverse genus of orchids. The name is from the Greek dendron (\"tree\") and bios (\"life\"); it means \"one who lives on trees\". They are either epiphytic, or occasionally lithophytic. They have adapted to a wide variety of habitats, from the high altitudes in the Himalayan mountains to lowland tropical forests and even to the dry climate of the Australian desert.",
                        hawaiianName: "Not Available",
                        species: "Dendrobium sp",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 42,
                        picture: "~/images/dichorisandra_thyrsiflora.jpg", commonName: "Blue ginger",
                        conservationStatus: "Low-risk",
                        description: "The blue ginger is a species of tropical flowering plant which resembles ginger in growth and habit but is actually related to the spiderworts (the genus Tradescantia). it is cultivated for its handsome spotted stems and large shiny foliage which is held horizontally, surmounted by striking blue flowers. The Latin specific epithet thyrsiflora means with flower clusters resembling thyme.",
                        hawaiianName: "Not Available",
                        species: "Dichorisandra thyrsiflora",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 43,
                        picture: "~/images/eichhornia_crassipes.jpg", commonName: "Common water hyacinth",
                        conservationStatus: "Low-risk",
                        description: "Commonly known as common water hyacinth, is an aquatic plant and often a highly problematic invasive species. One of the fastest growing plants known, water hyacinth reproduces primarily by way of runners or stolons, which eventually form daughter plants. Each plant additionally can produce thousands of seeds each year, and these seeds can remain viable for more than 28 years.",
                        hawaiianName: "Not Available",
                        species: "Eichhornia crassipes",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 44,
                        picture: "~/images/erythrina_crista-galli.jpg", commonName: "Cockspur coral tree",
                        conservationStatus: "Low-risk",
                        description: "Often known as the cockspur coral tree, is a flowering tree in the family Fabaceae. It is known by several common names such as ceibo, seibo, corticeira, and bucar. This species characteristically grows wild in gallery forest ecosystems along watercourses, as well as in swamps and wetlands. In urban settings, it is often planted in parks for its bright red flowers.",
                        hawaiianName: "Not Available",
                        species: "Erythrina crista-galli",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 45,
                        picture: "~/images/eucalyptus_deglupta.jpg", commonName: "Rainbow eucalyptus",
                        conservationStatus: "Low-risk",
                        description: "Commonly known as the rainbow eucalyptus, Mindanao gum, or rainbow gum. It is characterized by multi-colored bark featuring hues of blue, purple, orange and maroon. It thrives in rich, medium to wet soil in full sun and is intolerant of frost. In its native habitat, it grows up to 6 ft wide and over  250 ft tall.",
                        hawaiianName: "Not Available",
                        species: "Eucalyptus deglupta",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 46,
                        picture: "~/images/eugenia_uniflora.jpg", commonName: "Pitanga",
                        conservationStatus: "Low-risk",
                        description: "Commonly known as pitanga, Suriname cherry, Brazilian cherry, Cayenne cherry, or Cerisier Carre, is a plant in the family Myrtaceae. It is characterized by multi-colored bark featuring hues of blue, purple, orange and maroon. It thrives in rich, medium to wet soil in full sun and is intolerant of frost.",
                        hawaiianName: "Not Available",
                        species: "Eugenia uniflora",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 47,
                        picture: "~/images/ficus_microcarpa.jpg", commonName: "Chinese banyan",
                        conservationStatus: "Low-risk",
                        description: "Also known as Chinese banyan, Malayan banyan, Indian laurel, curtain fig, or gajumaru, is a tree in the fig family Moraceae. The largest known specimen is at the Menehune Botanical Gardens near Nawiliwili, Kauai, Hawai'i which is 110 ft in height, 250 ft in crown spread, and having over one thousand aerial trunks.",
                        hawaiianName: "Not Available",
                        species: "Ficus microcarpa",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 48,
                        picture: "~/images/filicium_decipiens.jpg", commonName: "Fern tree",
                        conservationStatus: "Low-risk",
                        description: "Known as fern tree, Japanese fern tree, Pihimbiya, or Thika palm, is a slow-growing tree with a straight, short trunk and a dense, neatly shaped rounded crown. It is a pleasant and graceful specimen whose small size makes it ideal for your yard or home landscape. The tree is most easily recognizable for its odd foliage.",
                        hawaiianName: "Not Available",
                        species: "Filicium decipiens",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 49,
                        picture: "~/images/gardenia_brighamii.jpg", commonName: "Forest gardenia",
                        conservationStatus: "Endangered",
                        description: "Commonly known as nanu, na'u, or forest gardenia, is a species of flowering plant in the coffee family, Rubiaceae, that is endemic to Hawaii. It is a small tree, reaching a height of 16 ft. The glossy, dark green leaves are ovate. The petals of the solitary, white flowers are fused at the base and have six lobes.",
                        hawaiianName: "Nanu",
                        species: "Gardenia brighamii",
                        status: "Endemic",
                        story: "Not Available",
                        uses: "Wood used for kapa anvils (kua kuku) (Abbott 1992:50). Fruit pulp used to make yellow kapa dye (Lamb 1981:134–135). In the Ethnology Collection at Bishop Museum there is a post-contact example of the wood made into a bowl."
                    }, {
                        class: 50,
                        picture: "~/images/gomphrena_globosa.jpg", commonName: "Globe amaranth",
                        conservationStatus: "Low-risk",
                        description: "Commonly known as globe amaranth, makhmali, and vadamalli, is an edible plant from the family Amaranthaceae. The round-shaped flower inflorescences are a visually dominant feature and cultivars have been propagated to exhibit shades of magenta, purple, red, orange, white, pink, and lilac. Within the flowerheads, the true flowers are small and inconspicuous.",
                        hawaiianName: "Not Available",
                        species: "Gomphrena globosa",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 51,
                        picture: "~/images/guaiacum_officinale.jpg", commonName: "Roughbark lignum-vitae",
                        conservationStatus: "Low-risk",
                        description: "Commonly known as roughbark lignum-vitae, guaiacwood or gaacwood, is a species of tree in the caltrop family named Zygophyllaceae. This small tree is very slow growing, reaching about 33 ft in height. The tree is essentially evergreen throughout most of its native range. The blue flowers have five petals that yield a bright-yellow-orange fruit with red flesh and black seeds.",
                        hawaiianName: "Not Available",
                        species: "Guaiacum officinale",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 52,
                        picture: "~/images/harpullia_pendula.jpg", commonName: "Tulipwood",
                        conservationStatus: "Low-risk",
                        description: "Known as the tulipwood or tulip lancewood, is a small to medium-sized rainforest tree. The tree's size, pleasant form and attractive fruit ensures its popularity of this ornamental tree. Tulipwood occurs in various types of rainforest, by streams or dry rainforests on basaltic or alluvial soils. In tropical and sub tropical rainforest. ",
                        hawaiianName: "Not Available",
                        species: "Harpullia pendula",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 53,
                        picture: "~/images/hedychium_coronarium.jpg", commonName: "White garland-lily",
                        conservationStatus: "Low-risk",
                        description: "Commonly known as white garland-lily or white ginger lily, is a perennial flowering plant in the Zingiberaceae (ginger) family. It is commonly cultivated in warm temperate and subtropical regions of the world as an ornamental and cultivated in China for use in medicine and production of aromatic oil due to its strong characteristic fragrance of the flowers said to be reminiscent of jasmine.",
                        hawaiianName: "Not Available",
                        species: "Hedychium coronarium",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 54,
                        picture: "~/images/hemigraphis_alternata.jpg", commonName: "Red ivy",
                        conservationStatus: "Low-risk",
                        description: "Also known as red ivy, red-flame ivy, or waffle plant, is a member of the Acanthaceae family. It is a prostrate plant with purple colored leaves. The leaves are hairy and opposite, and one leaf of a pair is much larger than the other.  The flowers of the plant grow from where the leaf meets the stem, and are white with purple penciling.",
                        hawaiianName: "Not Available",
                        species: "Hemigraphis alternata",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 55,
                        picture: "~/images/hibiscus_rosa-sinensis.jpg", commonName: "Chinese hibiscus",
                        conservationStatus: "Low-risk",
                        description: "Known colloquially as Chinese hibiscus, China rose, Hawaiian hibiscus, rose mallow or shoeblackplant, is a flowering plant in the Hibisceae tribe of the family Malvaceae. It is a bushy, evergreen shrub or small tree growing up to 16 ft tall, with glossy leaves and solitary, brilliant red flowers in summer and autumn with prominent orange-tipped red anthers.",
                        hawaiianName: "Not Available",
                        species: "Hibiscus rosa-sinensis",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 56,
                        picture: "~/images/hippeastrum_reticulatum.jpg", commonName: "Netted-vein amaryllis",
                        conservationStatus: "Low-risk",
                        description: "Commonly know as netted-veined amaryllis, is a flowering perennial herbaceous bulbous plant, in the Amaryllidaceae family. A defining characteristic of this species is an unusual and exquisite venation of the petals, darker than the purple to pink background color. The seeds are unusual for Hippeastrum in being orange-red, round, turgid and fleshy rather than black and paper like.",
                        hawaiianName: "Not Available",
                        species: "Hippeastrum reticulatum",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 57,
                        picture: "~/images/impatiens_wallerana.jpg", commonName: "Busy lizzie",
                        conservationStatus: "Low-risk",
                        description: "Also known as busy Lizzie, balsam, sultana, or simply impatiens, is a flowering herbaceous perennial plant growing up to 2 ft tall. Leaves are mostly alternate, although they may be opposite near the top of the plant. The stems are semi-succulent, and all parts of the plant (leaves, stems, flowers, roots) are soft and easily damaged.",
                        hawaiianName: "Not Available",
                        species: "Impatiens wallerana",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 58,
                        picture: "~/images/ixora_sp.jpg", commonName: "Ixora",
                        conservationStatus: "Low-risk",
                        description: "Common names include viruchi, rangan, kheme, ponna, chann tanea, techi, pan, siantan, jarum-jarum/jejarum, jungle flame, jungle geranium, cruz de Malta among others. Though native to the tropical and subtropical areas throughout the world, its centre of diversity is in Tropical Asia. It also grows commonly in subtropical climates in the United States, such as Florida where it is commonly known as West Indian Jasmine.",
                        hawaiianName: "Not Available",
                        species: "Ixora sp",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 59,
                        picture: "~/images/jasminum_sambac.jpg", commonName: "Arabian jasmine",
                        conservationStatus: "Low-risk",
                        description: "The Arabian jasmine, is a species of jasmine cultivated in many places for its attractive and sweetly fragrant flowers. It is a small shrub or vine growing up to 10 ft in height. The flowers may be used as a fragrant ingredient in perfumes and jasmine tea. It is the national flower of the Philippines, where it is known as sampaguita, as well as being one of the three national flowers of Indonesia, where it is known as melati putih.",
                        hawaiianName: "Not Available",
                        species: "Jasminum sambac",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 60,
                        picture: "~/images/justicia_brandegeana.jpg", commonName: "Mexican shrimp plant",
                        conservationStatus: "Low-risk",
                        description: "Mexican shrimp plant, shrimp plant or false hop, is an evergreen shrub in the genus Justicia of the family Acanthaceae. The flowers are white, extending from red bracts which look a bit like a shrimp, hence the shrub's common name, shrimp flower.The species is named after the American botanist Townshend Stith Brandegee.",
                        hawaiianName: "Not Available",
                        species: "Justicia brandegeana",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 61,
                        picture: "~/images/kigelia_africana.jpg", commonName: "Sausage tree",
                        conservationStatus: "Low-risk",
                        description: "Kigelia is a genus of flowering plants in the family Bignoniaceae. Other common names are sausage tree, cucumber tree, and sausage-like fruit. It is a bushy evergreen shrub growing to 3 ft tall. The stems and leaves are downy. The leaves are variegated and usually grow in clusters on the branches. As the plant receives more sun, the amount of creamy white on the speckled leaves will increase, and vice versa.",
                        hawaiianName: "Not Available",
                        species: "Kigelia africana",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 62,
                        picture: "~/images/koelreuteria_formosana.jpg", commonName: "Flamegold rain tree",
                        conservationStatus: "Low-risk",
                        description: "More commonly known as Flamegold rain tree or Taiwanese rain tree, is a deciduous tree up to 50 ft tall. It is widely grown throughout the tropics and sub-tropical parts of the world as a street tree. It flowers in early to mid-summer. Flowers are small and occur in branched clusters at the stem tips. They are butter-yellow with five petals that vary in length until opening.",
                        hawaiianName: "Not Available",
                        species: "Koelreuteria formosana",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 63,
                        picture: "~/images/lantana_montevidensis.jpg", commonName: "Trailing lantana",
                        conservationStatus: "Low-risk",
                        description: "Known by many common names, such as trailing lantana, weeping lantana, creeping lantana, small lantana, purple lantana or trailing shrubverbena. It is a small strongly scented flowering low shrub with oval-shaped green leaves. With support it has a climbing 'vine' form, when on edge a trailing form, and on the flat a groundcover form.",
                        hawaiianName: "Not Available",
                        species: "Lantana montevidensis",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 64,
                        picture: "~/images/leea_guineensis.jpg", commonName: "Leea",
                        conservationStatus: "Low-risk",
                        description: "Commonly called, West Indian holly, Hawaiian holly or burgundy leea, is a tropical evergreen shrub to small tree that typically grows in outdoor. This is an understory species that typically grows in its native habitat on forest floors in shady locations under the cover of taller trees where it typically adapts well to low light levels.",
                        hawaiianName: "Not Available",
                        species: "Leea guineensis",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 65,
                        picture: "~/images/litchi_chinensis.jpg", commonName: "Lychee",
                        conservationStatus: "Low-risk",
                        description: "Llitchi, liechee, liche, lizhi or li zhi, or lichee, is the sole member of the genus Litchi in the soapberry family, Sapindaceae. A tall evergreen tree, the lychee bears small fleshy fruits. The outside of the fruit is pink-red, roughly textured and inedible, covering sweet flesh eaten in many different dessert dishes. Since the perfume-like flavor is lost in the process of canning, the fruit is usually eaten fresh.",
                        hawaiianName: "Not Available",
                        species: "Litchi chinensis",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 66,
                        picture: "~/images/lonicera_japonica.jpg", commonName: "Japanese honeysuckle",
                        conservationStatus: "Low-risk",
                        description: "Known as golden-and-silver honeysuckle and Japanese honeysuckle, is a twining vine able to climb up to 33 ft high or more in trees. The flowers are double-tongued, opening white and fading to yellow, and sweetly vanilla scented. The fruit is a black spherical berry containing a few seeds. This species is often sold by American nurseries as the cultivar 'Hall's Prolific'.",
                        hawaiianName: "Not Available",
                        species: "Lonicera japonica",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 67,
                        picture: "~/images/lophostemon_confertus.jpg", commonName: "Brush box",
                        conservationStatus: "Low-risk",
                        description: "Common names include brush box, Queensland box, Brisbane box, pink box, box scrub, and vinegartree. In the wild its habitat ranges from moist open forest and rainforest ecotones, where it might reach heights of 130 ft or more, to coastal headlands where it acquires a stunted, wind-sheared habit. Dome-like in shape, it has a denser foliage with dark green, leathery leaves and hence provides more shade than eucalypts.",
                        hawaiianName: "Not Available",
                        species: "Lophostemon confertus",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 68,
                        picture: "~/images/magnolia_grandiflora.jpg", commonName: "Southern magnolia",
                        conservationStatus: "Low-risk",
                        description: "Commonly known as the southern magnolia or bull bay, is a tree of the family Magnoliaceae. Reaching 90 ft in height, it is a large striking evergreen tree. Although endemic to the lowland subtropical forests on the Gulf and south Atlantic coastal plain, it is widely cultivated in warmer areas around the world. The timber is hard and heavy, and has been used commercially to make furniture, pallets, and veneer.",
                        hawaiianName: "Not Available",
                        species: "Magnolia grandiflora",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 69,
                        picture: "~/images/mangifera_indica.jpg", commonName: "Mango",
                        conservationStatus: "Low-risk",
                        description: "Commonly known as mango, is a species of flowering plant in the sumac and poison ivy family Anacardiaceae. Hundreds of cultivated varieties have been introduced to other warm regions of the world. It is a large fruit-tree, capable of a growing to a height and crown width of about 100 ft and trunk circumference of more than 12 ft.",
                        hawaiianName: "Manako",
                        species: "Mangifera indica",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 70,
                        picture: "~/images/metrosideros_polymorpha.jpg", commonName: "Ohia lehua",
                        conservationStatus: "At-risk",
                        description: "The Ohi'a lehua, is a species of flowering evergreen tree in the myrtle family, Myrtaceae, that is endemic to the six largest islands of Hawaii. It is a highly variable tree, being up to 82 ft tall in favorable situations, and a much smaller prostrate shrub when growing in boggy soils or directly on basalt. It produces a brilliant display of flowers, made up of a mass of stamens, which can range from fiery red to yellow.",
                        hawaiianName: "Ohia lehua",
                        species: "Metrosideros polymorpha",
                        status: "Endemic",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 71,
                        picture: "~/images/musa_x_paradisiaca.jpg", commonName: "Banana",
                        conservationStatus: "Low RIsk",
                        description: "This is the accepted name for the hybrid between Musa acuminata and Musa balbisiana. Almost all cultivated plantains and many cultivated bananas are triploid cultivars of this species. It is believed that Southeast Asian farmers first domesticated M. acuminata. When the cultivated plants spread north-west into areas where M. balbisiana was native.",
                        hawaiianName: "Mai'a",
                        species: "Musa x paradisiaca",
                        status: "Polynesian Introduced",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 72,
                        picture: "~/images/nandina_domestica.jpg", commonName: "Sacred Bamboo",
                        conservationStatus: "Low Risk",
                        description: "Commonly known as nandina, heavenly bamboo or sacred bamboo, is a species of flowering plant in the family Berberidaceae. Despite the common name, it is not a bamboo but an erect evergreen shrub up to 7 ft tall, with numerous, usually unbranched stems growing from ground level. The glossy leaves are sometimes deciduous in colder areas.",
                        hawaiianName: "Not Available",
                        species: "Nandina domestica",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 73,
                        picture: "~/images/norantea_guianensis.jpg", commonName: "Red hot poker vine",
                        conservationStatus: "Low Risk",
                        description: "Commonly known as Red Hot Poker Vine, Red Popcorn, Conoro-antegri, or Karakara, is a large woody vine, climbing up to 30 ft with adventitious roots. Leaves glossy green, smooth and thick; young leaves orangey or reddish.Flowers small and insignificant, borne along middle axis of elongated terminal racemes.",
                        hawaiianName: "Not Available",
                        species: "Norantea guianensis",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 74,
                        picture: "~/images/orthosiphon_aristatus.jpg", commonName: "Cat's whiskers",
                        conservationStatus: "Low Risk",
                        description: "It is known as kumis kucing in Indonesia and misai kucing in Malaysia. In the US it may be commonly known as cat's whiskers or Java tea. It is mainly taken to stimulate urination. According to Indonesian and Malaysian folk medicine, bladder or kidney pain, gout, rheumatism and arteriosclerosis can be treated by drinking a decoction of leaves boiled in water.",
                        hawaiianName: "Not Available",
                        species: "Orthosiphon aristatus",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 75,
                        picture: "~/images/pandanus_tectorius.jpg", commonName: "Screw pine",
                        conservationStatus: "Low Risk",
                        description: "Common names include Tahitian screwpine, thatch screwpine, hala tree, pandanus, and pu hala in Hawaiian. The fruit is sometimes known as hala fruit. is a small tree that grows upright to reach up to 46 ft in height. It is supported by prop roots that firmly anchors the tree to the ground. Roots sometimes grow along the branch, and they grow a wide angles in proportion to the trunk.",
                        hawaiianName: "Hala",
                        species: "Pandanus tectorius",
                        status: "Indigenous",
                        story: "`Ōlelo Noeau: [I] ‘A‘ohe ‘alawa wale iho ia Mali‘o. Not even a glance at Mali‘o. Said of a haughty person. Pele was once so annoyed with Mali‘o and her brother Halaaniani that she turned them both into stone and let them lie in the sea in Puna, Hawai‘i. It was at a bay named after Halaaniani that clusters of pandanus were tossed into the sea as tokens to loved ones. These were borne by the current to Kamilo in Ka‘u. [II] ‘A‘ohe hala ‘ula i ka po. No hala fruit shows its color in the darkness of night. Beauty must be seen to be enjoyed. [III] He iki hala au no Kea‘au, ‘a‘ohe pohaku ‘ala e naha ai. I am a small hala fruit of Kea‘au, but there is no rock hard enough to smash me. The boast of a Puna man–I am small, perhaps, but mighty. [IV] He lauhala lana. Floating pandanus leaves. Said of people who drift from place to place; worthless vagabonds. [V] He pu hala a‘a kiolea. A hala tree with thin, hanging roots. Said of one who is not strong, like a tree with aerial roots that are not yet imbedded in the earth. [VI] He pu hala uo‘o. A tough [old] pandanus tree. Said of a stingy person. A play on pu hala in Puhala-hua, the name of a man in the 1800s who was known for his thrift and diligence in saving for old age. [VII] Hilo, nahele paoa i ke ‘ala. Hilo, where the forest is imbued with fragrance. Hilo's forest is fragrant with hala and lehua blossoms. [VIII] Hopu hewe a ka ‘ahui hala o Kekele. [One] grasps the pandanus cluster of Kekele by mistake. Said of one who meets with disappointment. Play on hala (to miss or be gone). The hala cluster is often used figuratively to refer to the scrotum. Kekele is a grove at the base of the Nu‘uanu Pali. [IX] Ka hala lau kalakala o Waiku. The thorny-leaved hala tree of Waiku. A boast about someone who is not to be tampered with. Ka hala mapu ‘a‘ala o Uoeloa. The sweet-scented hala of Upeloa. Upeloa, in Hilo, was noted for its sweet-smelling hala. [X] Ka makani hali ‘ala o Puna. The fragrance-bearing wind of Puna. Puna, Hawai‘i, was famed for the fragrance of maile, lehua, and hala. It was said that when the wind blew from the land, fishermen could smell the fragrance of these leaves and flowers. [XI] Ka ua kahiko hala o Kea‘au. The rain that adorns the pandanus trees of Kea‘au. Refers to the pandanus grove of Kea‘au, Puna, Hawai‘i. [XII] Ka ua kiki hala o Punalu‘u. The hala-pelting rain of Punalu‘u. Refers to the rain at Punalu‘u, O‘ahu. [XIII] Ka ua pe‘e pu hala o Huelo. The rain of Huelo that makes one hide in a hala grove. [XIV] Ka ua pehi hala o Hamakua. The rain of Hamakua that pelts the pandanus fruit clusters. Refers to Hamakua, Maui. [XV] Ka wahine alualu pu hala o Kamilo. The hala-pursuing woman of Kamilo. A current comes to Kamilo in Ka‘u from Halaaniani in Puna; whatever is tossed in the sea at Halaaniani floats into Kamilo. Papua once left her husband in Puna and went to Ka‘u. He missed her so badly that he decided to send her a pretty loincloth she had made him. This might make her think of him and come back. He wrapped the malo around a stem of a hala cluster, tied it securely in place with a cord, and tossed it into the sea. A few days later some women went fishing at Kamilo and noticed a hala cluster bobbing in the water. Eagerly they tried to sieze it until one of the women succeeded. Kapua watched as the string was untied and the malo unfolded. She knew that it was her husband's plea to come home, so she returned to Puna. [XVI] Lei Hanakahi i ke ‘ala me ke onaona o Pana‘ewa. Hanakahi is adorned with the fragrance and perfume of Pana‘ewa. The forest of Pana‘ewa was famous for its maile vines and hala and lehua blossoms, well liked for making lei, so Hilo (Hanakahi) was said to be wreathed in fragrance. [XVII] Ma‘ema‘e i ke kai ka pua o ka hala, ua ma‘ewa wale i ka poli o Kahiwa. Cleaned by the sea are the blossoms of the hala whose leaves sway at the bosom of Kahiwa. These two lines from a chant of praise for a chief are used as an expression of admiration. [XVIII] Ma‘ema‘e Puna i ka hala me ka lehua. Lovely is Puna with the hala and the lehua. Refers to Puna, Hawai‘i. [XIX] Moena haunu ‘ole o ka nahele. Mat of the forest to which no strips are added in making. Said of a bed made of fern, banana, or other leaves of the forest–one needs no strips of lauhala or other material to make a mat. [XX] Na hala o Kekele. The hala grove of Kekele. This grove, famous for the variety and fragrance of its hala, was found at the foot of Nu‘uanu Pali. Some people declare that although the hala trees have been cut down for many years, that they can still smell the fragrance in the breeze as they pass at night. [XXI] Na hala o Naue ‘au i ke kai. The hala of Naue swin out to sea. The hala trees of Naue, Kaua‘i, seem to reach out to sea. This expression is used in songs and chants. [XXII] Nani Puna po i ke ‘ala. Beautiful Puna, heavy with fragrance. Praise for Puna, Hawai‘i, where the wreath of maile, lehua, and hala blossoms are ever present. [XXIII] Na niu ulu ao‘a o Mokuola. The tall, slim coconuts of Mokuola. Mokuola (now called Coconut Island) in Hilo, is a place where pandanus and coconut trees were numerous. [XXIV] Pala ka hala, momona ka ha‘uke‘uke. When the pandanus fruit ripens, the ha‘uke‘uke sea urchin is fat. [XXV] Pala ka hala, momona ka uhu. When the pandanus fruit is ripe, the parrot fish is fat. The sea urchin, a favorite food of the parrotfish, is fat during the season when the pandanus fruit is ripe. Feeding on the sea urchin, the fish, too, becomes fat. [XXVI] Pala ka hala, ‘ula ka ‘a‘i. When the hala ripens, the neck is brightened by them. People are very fond of hala lei. From a name chant of Kuali‘i. [XXVII] Pe‘epe‘e pu hala. Hiders among the hala trees. An epithet for the kauwa of Hamakualoa, Maui. [XXVIII] Puhalu ka ihu, nana i ke ka‘ao. When the scent reaches the nose, one sees the overripe hala fruit [fallen to the ground]. One only notices many good things a person does when it is too late to show appreciation. [XXIX] Puna, kai nehe i ka ulu hala. Puna, where the sea murmurs to the hala grove. [XXX] Pu‘u i ka hala o Kekaha. Choked on the hala fruit of Kekaha. Pregnant.",
                        uses: "The hala fruit is made part of a treatment for ‘ea and pa‘ao‘ao. The aerial roots are used in medications for childbirth and a skin disorder. They are combination with pohepohe (Hydrocotyle verticillata), kohekohe (Eleocharis spp.), hala leaf buds, ‘ala‘ala wai nui pehu (Peperomia spp.), ‘ihi makole (Oxalis corniculata), naio leaf buds, fruit, and leaves (Myoporum sandwicense), niu (coconut, Cocos nucifera), kukui flowers (Aleurites moluccana), noni fruits (Morinda citrifolia), and kō (Saccharum officinarum). For childbirth, a treatment includes ‘uhaloa root (Waltheria indica), noni fruits, hala leaf buds and aerial roots, ‘ahu‘awa leaf buds (Cyperus javanicus), kō kea, and ‘alaea clay. For chest pains and kohepopo a drink of hala aerial roots, pa‘ihi (Nasturtium sarmentosum), ‘uhaloa, pōpolo root bark (Solanum  americanum), ‘ala‘ala wai nui pehu stems (Peperomia), ‘ohi‘a lehua bark (Metrosideros spp.), noni fruit, and kō kea) (Chun 1994:73–77).  Leaves are prepared and woven into mats and pillows, and thatch (Abbott 1992:71–75). Seeds and fruit are edible (Abbott 1992:72), and roots may be used as cordage fiber (Summers 1990:99–100). For some ‘uli‘uli (hula rattles) the handles were made of lauhala. Phalanges (fruit parts or \"keys\") used in lei & when dried, as brushes for painting kapa (Abbott 1992:54–55). In the Bishop Museum ethnology collection there are many beautiful hats made from the leaf of the hala tree and a post-contact example of the stem made into a bowl."
                    }, {
                        class: 76,
                        picture: "~/images/pentas_lanceolata.jpg", commonName: "Egyptian star cluster",
                        conservationStatus: "Low Risk",
                        description: "Commonly known as Egyptian starcluster, is known for its wide use as a garden plant where it often accompanies butterfly gardens. It is a tropical woody-based perennial or subshrub that grows 6 ft tall in its native habitat. It is also a many-branched, somewhat sprawling plant that features rounded clusters of star-shaped flowers over a long summer to frost bloom. ",
                        hawaiianName: "Not Available",
                        species: "Pentas lanceolata",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 77,
                        picture: "~/images/petrea_volubilis.jpg", commonName: "Sandpaper vine",
                        conservationStatus: "Low Risk",
                        description: "Petrea is a genus of evergreen flowering vines that have rough-textured leaves, hence the common name sandpaper vine. The tubular blue flowers only last a few days but the larger and more showy bluish purple calyces remain, fading first to blue and finally to a pale gray color. The dark green foliage acts as a foil to the pale calyces, so that the floral display appears as pale stars on a dark background.",
                        hawaiianName: "Not Available",
                        species: "Petrea volubilis",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 78,
                        picture: "~/images/phytolacca_dioica.jpg", commonName: "Ombu",
                        conservationStatus: "Low Risk",
                        description: "Commonly known as omb, is a massive evergreen tree and has an umbrella-like canopy that spreads to a diameter up to 50 ft and can attain a height up to 60 ft. Because it is derived from herbaceous ancestors, its trunk consists of anomalous secondary thickening rather than true wood. As a result, the omb grows fast but its wood is soft and spongy enough to be cut with a knife.",
                        hawaiianName: "Not Available",
                        species: "Phytolacca dioica",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 79,
                        picture: "~/images/plectranthus_scutellarioides.jpg", commonName: "Coleus",
                        conservationStatus: "Low Risk",
                        description: "Commonly known as coleus, is a species of flowering plant in the family Lamiaceae. Another common name is painted nettle, reflecting its relationship to deadnettles. Typically growing to 2 ft tall and wide, it is a bushy, woody-based evergreen perennial, widely grown for the highly decorative variegated leaves found in cultivated varieties.",
                        hawaiianName: "Not Available",
                        species: "Plectranthus scutellarioides",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 80,
                        picture: "~/images/podranea_ricasoliana.jpg", commonName: "Pink trumpet vine",
                        conservationStatus: "Low Risk",
                        description: "Podranea, is a genus of one or two species of African flowering vines in the Bignoniaceae family. It is a very showy plant with its glossy foliage and abundance of attractive pink flowers. It is also a vigorous, woody, rambling, evergreen climber without tendrils. The leaves are compound and a deep glossy green.",
                        hawaiianName: "Not Available",
                        species: "Podranea ricasoliana",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 81,
                        picture: "~/images/portulacaria_afra.jpg", commonName: "Elephant bush",
                        conservationStatus: "Low Risk",
                        description: "Also known as elephant bush, dwarf jade plant, porkbush, and spekboom, is a small-leaved succulent plant. It is a soft-wooded, semi-evergreen upright shrub or small tree, usually up to 15 ft tall. It is popular as an indoor bonsai, and as a hardy xeriscaping plant. Several varieties exist - some bred in cultivation, others naturally occurring.",
                        hawaiianName: "Not Available",
                        species: "Portulacaria afra",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 82,
                        picture: "~/images/punica_granatum.jpg", commonName: "Pomegranate",
                        conservationStatus: "Low Risk",
                        description: "The pomegranate is a fruit-bearing deciduous shrub or small tree in the family Lythraceae that grows up to 33 ft tall. As intact arils or juice, pomegranates are used in baking, cooking, juice blends, meal garnishes, smoothies, and alcoholic beverages, such as cocktails and wine. The French term for pomegranate, grenade, has given its name to the military grenade.",
                        hawaiianName: "Not Available",
                        species: "Punica granatum",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 83,
                        picture: "~/images/pyrostegia_venusta.jpg", commonName: "Flamevine",
                        conservationStatus: "Low Risk",
                        description: "Also commonly known as flamevine or orange trumpetvine, is a plant species of the genus Pyrostegia of the family Bignoniaceae, nowadays a well-known garden species. It is one of the most spectacular flowering vines in cultivation. It is a vigorous, evergreen liana (a name for large woody climbers) that can spread quickly by tendrils to the top of whatever supports it.",
                        hawaiianName: "Not Available",
                        species: "Pyrostegia venusta",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 84,
                        picture: "~/images/quisqualis_indica.jpg", commonName: "Chinese honeysuckle",
                        conservationStatus: "Low Risk",
                        description: "Also known as the Chinese honeysuckle or Rangoon creeper, is a vine with red flower clusters. The Rangoon creeper is a ligneous vine that can reach up to 26 ft. The leaves are elliptical with an acuminate tip and a rounded base, and the flowers are fragrant and tubular and their color varies from white to pink to red. ",
                        hawaiianName: "Not Available",
                        species: "Quisqualis indica",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 85,
                        picture: "~/images/rhaphiolepis_umbellata.jpg", commonName: "Indian hawthorn",
                        conservationStatus: "Low Risk",
                        description: "This is a species of flowering plant in the Rosaceae family. Growing to 5 ft tall and wide, it is an evergreen shrub with glossy oval leaves, and scented white flowers, sometimes tinged with pink, in early summer. This plant has gained the Royal Horticultural Society's Award of Garden Merit. It is used in Japan as an astringent and a dyeing agent.",
                        hawaiianName: "Not Available",
                        species: "Rhaphiolepis umbellata",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 86,
                        picture: "~/images/solanum_seaforthianum.jpg", commonName: "Brazillian nightshade",
                        conservationStatus: "Low Risk",
                        description: "The Brazilian nightshade, is a flowering evergreen vine of the Solanaceae family. It is characterized by clusters of four to seven leaves and can climb to a height of 20 ft given enough room. It blooms in the mid to late summer with clusters of star-shaped purple inflorescence followed by scarlet marble-sized berries. The plant is highly heat resistant, but cannot tolerate frost conditions.",
                        hawaiianName: "Not Available",
                        species: "Solanum seaforthianum",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 87,
                        picture: "~/images/stemmadenia_littoralis.jpg", commonName: "Milky way tree",
                        conservationStatus: "Low Risk",
                        description: "The milky way tree is an open-branching tree that creates a multi-layered canopy. In the tropics, these trees have a maximum height of around 25 ft. The tubular white flowers of Stemmadenia littoralis can be found on the tree from spring through fall. Only when the cool winter nights set in does the tree stop flowering. While in flower, it is a remarkably floriferous tree.",
                        hawaiianName: "Not Available",
                        species: "Stemmadenia littoralis",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 88,
                        picture: "~/images/strelitzia_reginae.jpg", commonName: "Bird of paradise",
                        conservationStatus: "Low Risk",
                        description: "Common names include strelitzia, crane flower or bird of paradise, though these names are also collectively applied to other species in the genus Strelitzia. The plant grows to 6.6 ft tall, with large, strong leaves. They are evergreen leaves and arranged in two ranks, making a fan-shaped crown. The flowers stand above the foliage at the tips of long stalks. ",
                        hawaiianName: "Not Available",
                        species: "Strelitzia reginae",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 89,
                        picture: "~/images/symphytum_officinale.jpg", commonName: "Common Comfrey",
                        conservationStatus: "Low Risk",
                        description: "Other names include Quaker comfrey, cultivated comfrey, boneset, knitbone, consound, and slippery-root. The hardy plant can grow to a height of 4 ft. Its roots have been used in the traditional Balkan medicine internally (as tea or tincture) or externally (as ointment, compresses,or alcoholic digestion) for treatment of disorders of the locomotor system and gastrointestinal tract.",
                        hawaiianName: "Not Available",
                        species: "Symphytum officinale",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 90,
                        picture: "~/images/tabebuia_impetiginosa.jpg", commonName: "Pink trumpet Tree",
                        conservationStatus: "Low Risk",
                        description: "Known as pink ipe, pink lapacho, or pink trumpet tree is a native tree of family Bignoniaceae. It is a conspicuous and well-known species with a long history of human use. Consequently, it has a range of local names: ipe-cavata, ipe-comum, ipe-reto, ipe-rosa, ipe-roxo-damata, lapacho negro, pau d'arco-roxo, peuva or piuva.",
                        hawaiianName: "Not Available",
                        species: "Tabebuia impetiginosa",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 91,
                        picture: "~/images/tabernaemontana_divaricata.jpg", commonName: "Pinwheel flower",
                        conservationStatus: "Low Risk",
                        description: "Apocynaceae, commonly called pinwheelflower, crape jasmine, East India rosebay and Nero's crown is an evergreen shrub. The plant generally grows to a height of 5-6 ft and is dichotomously-branched. The large shiny leaves are deep green. The waxy blossoms are found in small clusters on the stem tips. The plant blooms in spring but flowers appear sporadically all year. ",
                        hawaiianName: "Not Available",
                        species: "Tabernaemontana divaricata",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 92,
                        picture: "~/images/tamarindus_indica.jpg", commonName: "Tamarind",
                        conservationStatus: "Low Risk",
                        description: "Tamarind is a leguminous tree in the family Fabaceae. The genus Tamarindus is a monotypic taxon, having only a single species. The tamarind tree produces pod-like fruit, which contain an edible pulp that is used in cuisines around the world. Other uses of the pulp include traditional medicine and metal polish. The wood can be used for woodworking, and tamarind seed oil can be extracted from the seeds.",
                        hawaiianName: "Not Available",
                        species: "Tamarindus indica",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 93,
                        picture: "~/images/terminalia_catappa.jpg", commonName: "Indian almond",
                        conservationStatus: "Low Risk",
                        description: "It is known by the English common names country-almond, Indian-almond, Malabar-almond, sea-almond, tropical-almond and false kamani. The tree grows up to 115 ft tall, with an upright, symmetrical crown and horizontal branches. Terminalia catappa has corky, light fruit that are dispersed by water. The seed within the fruit is edible when fully ripe, tasting almost like almond.",
                        hawaiianName: "Not Available",
                        species: "Terminalia catappa",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 94,
                        picture: "~/images/thunbergia_battescombei.jpg", commonName: "Blue glory vine",
                        conservationStatus: "Low Risk",
                        description: "Known as the scrambling sky flower, is a herbaceous weak stemmed perennial vine that tends to lean upon other plants for support. So scrambling clock vine is a herbaceous weak stemmed perennial vine that tends to lean upon other plants for support. When unsupported it will form a symmetrical mound of flopped over stems that is about 4 ft high by 6 ft wide. ",
                        hawaiianName: "Not Available",
                        species: "Thunbergia battescombei",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 95,
                        picture: "~/images/tipuana_tipu.jpg", commonName: "Rosewood",
                        conservationStatus: "Low Risk",
                        description: "Also known as tipa, rosewood, and pride of Bolivia, is the only member of the genus Tipuana and well-known for its use as a shade tree. It is viewed as an invasive weed in some countries and is known for having a very aggressive root system. The tree roots can easily lift up concrete and asphalt. Precautions should be taken when planting near buildings, homes, or pools, as they are likely to be damaged.",
                        hawaiianName: "Not Available",
                        species: "Tipuana tipu",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 96,
                        picture: "~/images/tradescantia_spathacea.jpg", commonName: "Boat lily",
                        conservationStatus: "Low Risk",
                        description: "The boatlily or Moses-in-the-cradle, has fleshy rhizomes and rosettes of waxy lance-shaped leaves. Leaves are dark to metallic green above, with glossy purple underneath. It has fleshy rhizomes and rosettes of waxy lance-shaped leaves. Leaves are dark to metallic green above, with glossy purple underneath. They are very attractive foliage plants that will reach 1 ft tall.",
                        hawaiianName: "Not Available",
                        species: "Tradescantia spathacea",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 97,
                        picture: "~/images/turnera_ulmifolia.jpg", commonName: "Yellow alder",
                        conservationStatus: "Low Risk",
                        description: "The ramgoat dashalong or yellow alder, is a species of plant of family Passifloraceae. It grows erect, with dark toothed leaves and small, yellow-orange flowers, and is often found as a weed growing on roadsides. This plant is commonly misidentified with the closely related T. diffusa in horticultural commerce, causing it to be often misrepresented as \"Damiana.\"",
                        hawaiianName: "Not Available",
                        species: "Turnera ulmifolia",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }, {
                        class: 98,
                        picture: "~/images/vitex_rotundifolia.jpg", commonName: "Beach vitex",
                        conservationStatus: "Low Risk",
                        description: "The roundleaf chastetree or beach vitex is a species of Vitex, this woody perennial plant typically grows approximately 3 ft in height. Its range includes continents and islands stretching from India east to Hawaii and from Korea south to Australia. It has a sprawling growth habit and produces runners that root regularly at nodes.",
                        hawaiianName: "Pohinahina",
                        species: "Vitex rotundifolia",
                        status: "Indigenous",
                        story: "",
                        uses: "Can be smashed into a kapai or poultice to be used as an insect repellant, and also can be used for the soothing of itches and rashes."
                    }, {
                        class: 99,
                        picture: "~/images/youngia_japonica.jpg", commonName: "Oriental false hawksbeard",
                        conservationStatus: "Low Risk",
                        description: "Commonly called Oriental false hawksbeard, is a species of flowering plant in the aster family. Native to eastern Asia, it is now found as a weed nearly worldwide. It is an annual that produces yellow flowers. In tropical areas, it can bloom year round, while in temperate areas it blooms in late spring and early summer. Stems are usually solitary and erect. Basal leaves are large a pinnately divided. Its fruits are wind dispersed.",
                        hawaiianName: "Not Available",
                        species: "Youngia japonica",
                        status: "Invasive",
                        story: "Not Available",
                        uses: "Not Available"
                    }]
            }
        },
        methods: {
            onItemTap(e) {
                this.$emit("select", e.item);
                this.$navigateTo(PlantDetails, {props: {plant: e.item}});
            },
            lambdaExample() {
                axios.get('https://01b33zw9g9.execute-api.us-east-1.amazonaws.com/dev/mea-kanu').then(response => {
                    console.log(response);
                    console.log(response.data);
                });
            },
            openCam() {
                this.isBusy = true;
                camera.requestPermissions();
                // console.log("1");
                camera
                    .takePicture({
                        width: 300,
                        height: 300,
                        keepAspectRatio: true,
                        saveToGallery: true
                    }).then(imageAsset => {
                    // console.log("2");
                    console.log("This is the imageAsset output");
                    console.log(imageAsset);
                    this.picture = imageAsset;
                    // console.log("5");
                    let source = new imageSource.ImageSource();
                    // console.log("6");
                    source.fromAsset(imageAsset).then(source => {
                        // console.log("4");
                        this.pictureBase64String = source.toBase64String("jpg", 100);
                        console.log(this.pictureBase64String);
                        // console.log("Here I am");
                        axios({
                            method: "post",
                            url: "http://168.105.244.121:8081",
                            data: {ImageContent: this.pictureBase64String.toString()},
                            headers: {"Content-Type": "application/json"}
                        }).then(response => {
                            let result = response.data;
                            this.percentages = result.Percents;
                            let plants = [];
                            console.log("a");
                            console.log(result);
                            console.log(result.PNO);
                            console.log(result.PNO[0]);
                            console.log(result.PNO[1]);
                            console.log("b");
                            console.log(this.percentages);
                            for (const value of result.PNO) {
                                console.log(this.plantList[value]);
                                plants.push(this.plantList[value]);
                            }
                            console.log("c");
                            console.log(plants[0]);
                            console.log(plants[0].hawaiianName);
                            console.log(plants[1]);
                            //console.log("Success: firebase is responding to your shit");
                            this.$navigateTo(PlantResults, {
                                props: {
                                    plantResults: plants,
                                    percentages: result.Percents
                                }
                            });
                            console.log(result);

                        }, error => {
                            console.error(error);
                        });
                    });


                });
                this.picture = null;
            },
            uploadPicture() {
                var imageModule = require("tns-core-modules/ui/image");

                console.log("Hitting uploadPicture");
                //this.isBusy = true;
                let context = imagepicker.create({mode: "single"});
                context
                    .authorize()
                    .then(function () {
                        console.log("fuck1");
                        return context.present();
                    })
                    .then(function (selection) {
                        console.log("fuck2");
                        let source = new imageSource.ImageSource();
                        console.log("fuck3");
                        source.fromAsset(selection[0]).then(source => {
                            console.log("4");
                            console.log("Here I am");
                            http.request({
                                url: "http://72.130.247.31:8080",
                                method: "POST",
                                headers: { "Content-Type":"application/json" },
                                content:{
                                    ImageContent : source.toBase64String("jpg", 100)
                                }
                            })
                            // axios.post("https://plant-info-mea-kanu.firebaseio.com/data.json", {ImageContent: source.toBase64String("jpg", 100).toString()})
                            .then(response => {
                                console.log(response);
                                console.log(response.data);
                                let result = response.data;

                                // this.percentages = result.Percents;
                                // let plants = [];
                                // console.log("a");
                                // console.log(result.PNO);
                                // console.log(result.PNO[0]);
                                // console.log(result.PNO[1]);
                                // console.log("b");
                                // console.log(this.percentages);
                                // for (const value of result.PNO) {
                                //     console.log(this.plantList[value]);
                                //     plants.push(this.plantList[value]);
                                // }
                                // console.log("c");
                                // console.log(plants[0]);
                                // console.log(plants[0].hawaiianName);
                                // console.log(plants[1]);
                                // //console.log("Success: firebase is responding to your shit");
                                // this.$navigateTo(PlantResults, {
                                //     props: {
                                //         plantResults: plants,
                                //         percentages: result.Percents
                                //     }
                                // });
                                console.log("printing output of result");
                                console.log(result);

                            }, error => {
                                console.error(error);
                            });
                        });


                        // axios.post('http://72.130.247.31:8081', {ImageContent: source.toBase64String("jpg", 100).toString()})
                        //     .then(response => {
                        //         let result = response.data;
                        //         //this.results = result.PNO;
                        //         // if (result.hasOwnProperty('PNO') && result.hasOwnProperty('Percents')) {
                        //         this.isBusy = false;
                        //
                        //         this.percentages = result.Percents;
                        //         console.log("a");
                        //         console.log(result.PNO);
                        //         console.log("b");
                        //         console.log(this.percentages);
                        //         let plants = [];
                        //         //console.log(this.results);
                        //         for (const value of result.PNO) {
                        //             plants.push(this.plantList[value]);
                        //         }
                        //         console.log("c");
                        //         console.log(plants);
                        //         //console.log("Success: firebase is responding to your shit");
                        //         this.$navigateTo(PlantResults, {
                        //             props: {
                        //                 plantResults: plants,
                        //                 percentages: result.Percents
                        //             }
                        //         });
                        //         console.log(result);
                        //     }, error => {
                        //         console.log("HEREIAM");
                        //         console.error(error);
                        //     });

                    });
            },
        }
    }
</script>

<style scoped lang="scss">
    @import '../app-variables';
    // End custom common variables

    // Custom styles
    .list-picture {
        height: 100;
        width: 100;
    }

    .list-group {
        .list-group-item-content {
            padding: 8 15 4 15;
            background-color: $background-light;
        }

        .list-group-item-text {
            margin: 2 3;
        }

        .fa {
            color: $accent-dark;
        }
    }

    .back {
        background-color: gray;
    }
</style>
