import type { TemplateConfig } from "./configType";
import * as fs from 'fs';
const templateConfig: TemplateConfig = {
  name: "Nightly Bible",
  seo: {
    title: "Nightly Bible",
    description: "Nightly Bible Verses, Background music, Faith Grow and accompany you on your spiritual journey while sleeping.",
  },
  // Draws grid behind main container
  backgroundGrid: false,
  logo: "/logo.png",
  theme: "sunset",
  // Forces theme to be chosen above, no matter what user prefers
  forceTheme: true,
  // Shows switch to toggle between dark and light modes
  showThemeSwitch: false,
  // appStoreLink: "/",  // TODO: fix this 
  // "https://apps.apple.com/us/app/google/id234556",
  // googlePlayLink: "/", // TODO: fix this
  // "https://play.google.com/store/apps/details?id=com.nightlybible.app",
  localLink: "/app/android/nightlybible.apk",
  footer: {
    legalLinks: {
      termsAndConditions: true,
      cookiesPolicy: true,
      privacyPolicy: true,
    },
    socials: {
      instagram: "https://instagram.com/google",
      facebook: "https://facebook.com/google",
      twitter: "https://x.com/google",
    },
    links: [
      // { href: "/#features", title: "Features" },
      // { href: "/#how-it-works", title: "How it works" },
      // { href: "/#pricing", title: "Pricing" },
      // { href: "/#faq", title: "FAQ" },
    ],
  },
  topNavbar: {
    // cta: "Get the app",
    disableWidthAnimation: true,
    hideAppStore: true, // TODO: fix this
    hideGooglePlay: true, // TODO: fix this
    links: [
      // { href: "/#features", title: "Features" },
      // { href: "/#how-it-works", title: "How it works" },
      // { href: "/#pricing", title: "Pricing" },
      // { href: "/#faq", title: "FAQ" },
    ],
  },
  // appBanner: {
  //   id: "app-banner",
  //   title: "Download Our Mobile App Today!",
  //   subtitle:
  //     "Unlock the full potential of our services with seamless access at your fingertips. Stay connected, informed, and in control wherever you are.",
  //   screenshots: [
  //     "/screenshots/1.webp",
  //     "/screenshots/2.webp",
  //     "/screenshots/3.webp",
  //   ],
  // },
  home: {
    seo: {
      title: "Nightly Bible",
      description: "Nightly Bible Verses with Soothing Background Music—Nurture Your Faith and Feel Guided on Your Spiritual Journey as You Sleep.",
    },
    // testimonials: {
    //   id: "testimonials",
    //   title: "Testimonials",
    //   subtitle: "Check out a few of our customer stories",
    //   cards: [
    //     {
    //       name: "Alice Johnson",
    //       comment:
    //         "The service was fantastic! Highly recommended. The team was very professional and attentive to our needs. They went above and beyond to ensure we were satisfied with the results. I will definitely be using their services again in the future.",
    //     },
    //     {
    //       name: "Bob Smith",
    //       comment:
    //         "Great value for the price. Very satisfied with the overall experience. The product quality is top-notch and the customer service is excellent. I appreciate the prompt responses to my inquiries and the helpful advice provided. Highly recommend.",
    //     },
    //     {
    //       name: "Charlie Brown",
    //       comment:
    //         "An excellent experience from start to finish. The onboarding process was smooth and the support team was very responsive. I felt valued as a customer and the results exceeded my expectations. I am impressed with the level of detail and care put into their work.",
    //     },
    //     {
    //       name: "Dana White",
    //       comment:
    //         "Superb customer service and high-quality products. The team demonstrated great expertise and patience throughout the project. They addressed all my concerns and provided valuable insights. The end product was delivered on time and surpassed my expectations.",
    //     },
    //     {
    //       name: "Eve Adams",
    //       comment:
    //         "I couldn't be happier with the results! The attention to detail and the level of customization provided was outstanding. The team was friendly and professional, making the entire process enjoyable. I highly recommend their services to anyone looking for top-quality work.",
    //     },
    //   ],
    // },
    // partners: {
    //   title: "As seen on",
    //   logos: [
    //     "/misc/companies/apple.svg",
    //     "/misc/companies/aws.svg",
    //     "/misc/companies/google.svg",
    //     "/misc/companies/tumblr.svg",
    //   ],
    // },
    howItWorks: {
      id: "how-it-works",
      title: "How it works",
      subtitle:
        "As easy as 1, 2, 3",
      steps: [
        {
          title: "Install the App",
          subtitle:
            "Download and install the app on your device to get started quickly and easily.",
          image: "/stock/01.webp",
        },
        {
          title: "Charge your phone and let it play",
          subtitle:
            "The app recites Bible verses gently with soothing background music to help you fall asleep. Let the words of God guide you into deep, restorative sleep, so you wake up refreshed, energized, and ready to embrace the day ahead.",
          image: "/stock/02.webp",
        },
        {
          title: "Wake up refreshed",
          subtitle:
            "Wake up refreshed and energized, ready to embrace a new day, with love from God.",
          image: "/stock/03.webp",
        }
      ],
    },
    // features: {
    //   id: "features",
    //   title: "Grow faith while you sleep",
    //   subtitle:
    //     "You faith grows, silently, but strongly, even without you being aware.",
    //   cards: [
    //     {
    //       title: "Seamless Integration",
    //       subtitle:
    //         "Connect effortlessly with all your devices, ensuring smooth and efficient workflows across different platforms and applications without any disruptions",
    //       icon: "/3D/link-front-color.webp",
    //     },
    //     {
    //       title: "24/7 Customer Support",
    //       subtitle:
    //         "Get assistance whenever you need it with our dedicated customer support team, available around the clock to help resolve any issues you may encounter",
    //       icon: "/3D/clock-front-color.webp",
    //     },
    //     {
    //       title: "Intuitive Design",
    //       subtitle:
    //         "Navigate through our intuitive and easy-to-use interface designed to enhance user experience, making it accessible for users of all skill levels",
    //       icon: "/3D/roll-brush-front-color.webp",
    //     },
    //     {
    //       title: "Top-Notch Security",
    //       subtitle:
    //         "Protect your data with our top-notch security protocols, offering robust encryption and real-time monitoring to keep your information safe and secure",
    //       icon: "/3D/sheild-front-color.webp",
    //     },
    //   ],
    // },
    // faq: {
    //   id: "faq",
    //   title: "Frequently Asked Questions",
    //   qa: [
    //     {
    //       question: "How can I create an account on your website?",
    //       answer:
    //         "To create an account, click on the 'Sign Up' button located at the top right corner of our homepage. Fill in the required information, including your name, email address, and password. Once you submit the form, you will receive a confirmation email. Click the link in the email to verify your account, and you're all set!",
    //     },
    //     {
    //       question: "What payment methods do you accept?",
    //       answer:
    //         "We accept a variety of payment methods to ensure convenience for our customers. These include major credit cards (Visa, MasterCard, American Express), PayPal, Apple Pay, and Google Pay. For more details, visit our Payments page.",
    //     },
    //     {
    //       question: "How can I track my order?",
    //       answer:
    //         "Once your order is shipped, you will receive an email with a tracking number. You can use this tracking number on our website under the 'Track Order' section to see the current status and estimated delivery date of your package.",
    //     },
    //     {
    //       question: "What is your return policy?",
    //       answer:
    //         "We offer a 30-day return policy for unused and unopened items. If you are not satisfied with your purchase, please contact our customer support team to initiate a return. Refunds will be processed within 7-10 business days after we receive the returned item.",
    //     },
    //     {
    //       question: "How can I contact customer support?",
    //       answer:
    //         "You can contact our customer support team through the 'Contact Us' page on our website. We are available via email, phone, and live chat. Our support hours are Monday to Friday, 9 AM to 5 PM.",
    //     },
    //   ],
    // },
    header: {
      headline: "Drift Into Peaceful Rest with the Word of God",
      subtitle:
        "Let calming, spoken Bible verses fill your nights with faith and tranquility. Allow the soothing words to guide you into deep, restorative sleep, so you wake up refreshed, energized, and ready to embrace the day ahead.",
      screenshots: [
        "/screenshots/1.png",
        "/screenshots/2.png",
      ],
      // rewards: ["App of the year \n 1st", "Product of the day"], // TODO : fix this
      // usersDescription: "100+ people already using the app",
      headlineMark: [100, 100],
    },
    // pricing: {
    //   id: "pricing",
    //   title: "Pricing",
    //   subtitle: "Flexible costs to meet your budget",
    //   actionText: "Download the app",
    //   plans: [
    //     {
    //       title: "Basic Plan",
    //       price: "$9.99/month",
    //       rows: ["Access to basic features", "Email support", "1 GB storage"],
    //     },
    //     {
    //       title: "Standard Plan",
    //       price: "$19.99/month",
    //       featured: true,
    //       rows: [
    //         "Access to all basic features",
    //         "Priority email support",
    //         "10 GB storage",
    //         "Monthly webinars",
    //       ],
    //     },
    //     {
    //       title: "Premium Plan",
    //       price: "$29.99/month",
    //       rows: [
    //         "Access to all features",
    //         "24/7 support",
    //         "100 GB storage",
    //         "Weekly webinars",
    //         "Exclusive content",
    //       ],
    //     },
    //   ],
    // },
  },
  privacyPolicy: {
    seo: {
      title: "Privacy Policy - Mobile App Landing Template",
      description: "Privacy Policy",
    },
    content: fs.readFileSync("./src/docs/PRIVACY_POLICY.md", "utf-8"),
  },
  cookiesPolicy: {
    seo: {
      title: "Cookies Policy - Mobile App Landing Template",
      description: "Cookies Policy",
    },
    content: fs.readFileSync("./src/docs/COOKIES_POLICY.md", "utf-8"),
  },
  termsAndConditions: {
    seo: {
      title: "Terms and conditions - Mobile App Landing Template",
      description: "Terms and conditions",
    },
    content: fs.readFileSync("./src/docs/TERMS_AND_CONDITIONS.md", "utf-8"),
  },
};

export default templateConfig;
