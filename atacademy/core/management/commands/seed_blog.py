from django.core.management.base import BaseCommand
from core.models import Blog


class Command(BaseCommand):
    help = 'Seed the welcome blog post'

    def handle(self, *args, **options):
        slug = 'welcome-to-at-academy-empowering-tech-leaders'
        content = """Welcome to AT Academy: Empowering Tech Leaders for Over 6 Years

The technology landscape is evolving at a breakneck pace. From the silicon chips powering our devices to the AI algorithms shaping our decisions, staying ahead of the curve requires more than just textbook knowledge — it demands hands-on expertise and industry-aligned training.

Welcome to AT Academy (Amal Tej Academy). For over six years, we have been at the forefront of technical education, bridging the gap between academic learning and industry demands. With a legacy of transforming passionate learners into highly sought-after tech professionals, we are thrilled to announce our latest roster of comprehensive, industry-grade courses.

Whether you are a fresh graduate looking to launch your career or a working professional aiming to upskill, AT Academy offers a specialized pathway for you. Here is a thorough breakdown of the cutting-edge courses we offer.

Hardware & Core Engineering

1. Embedded Systems
The modern world runs on embedded systems — from smart appliances to automotive controllers. This course takes you deep into the intersection of hardware and software.
Core Curriculum: Master microcontrollers (8051, AVR, ARM Cortex-M), C and embedded C++ programming, and sensor interfacing.
Advanced Topics: Dive into Real-Time Operating Systems (RTOS), memory management, and communication protocols (I2C, SPI, UART, CAN).
Outcomes: You will learn to design, program, and debug dedicated hardware systems that operate efficiently under strict timing and memory constraints.

2. VLSI (Very Large Scale Integration)
For those fascinated by what happens inside a microchip, our VLSI program provides the specialized skills needed for the semiconductor industry.
Core Curriculum: Digital logic design, CMOS theory, and hardware description languages like Verilog and SystemVerilog.
Advanced Topics: ASIC design flow, FPGA prototyping, logic synthesis, and physical design (floorplanning, placement, and routing).
Outcomes: Students will gain the ability to design complex integrated circuits and understand the complete silicon lifecycle from RTL (Register-Transfer Level) to GDSII.

3. IoT (Internet of Things)
Connect the physical world to the digital realm. The IoT course bridges embedded hardware with cloud networks to create smart, interconnected environments.
Core Curriculum: Working with development boards like Raspberry Pi and NodeMCU, sensor data acquisition, and edge computing.
Advanced Topics: Communication protocols (MQTT, CoAP), IoT security, cloud integration (AWS IoT, Azure IoT), and building custom dashboards.
Outcomes: You will be able to architect end-to-end IoT solutions, from programming edge devices to deploying data analytics in the cloud.

Software Development & Cloud

4. Full Stack Python Development
Python remains the undisputed king of versatile programming. This course molds you into a complete web developer capable of handling both the client and server sides.
Front-End: HTML5, CSS3, JavaScript (ES6+), and modern UI frameworks like React or Vue.js.
Back-End: Deep dive into Python, mastering frameworks like Django and FastAPI for robust server-side logic.
Database & Deployment: SQL (PostgreSQL/MySQL), ORM integration, RESTful API development, and version control using Git.

5. Full Stack Java Development
Enterprise-scale applications rely heavily on Java. This course is designed to make you an enterprise-ready developer.
Front-End: Building dynamic user interfaces using Angular or React alongside core web technologies.
Back-End: Core Java (OOP, multithreading, collections), Spring Boot, and Hibernate for rapid backend development.
Database & Deployment: Microservices architecture, JDBC, building scalable REST APIs, and containerizing applications with Docker.

6. AWS + DevOps Cloud
The era of manual server management is over. This course merges cloud infrastructure with continuous delivery to streamline the software development lifecycle.
Cloud Infrastructure: Comprehensive training on Amazon Web Services (EC2, S3, VPC, RDS, IAM, Lambda).
DevOps Tools: Version control (Git), continuous integration and continuous deployment (CI/CD) pipelines using Jenkins or GitLab CI.
Automation & Orchestration: Infrastructure as Code (IaC) using Terraform, configuration management (Ansible), and container orchestration with Docker and Kubernetes.

Data, AI & Security

7. Data Science
Data is the new oil, and this course teaches you how to refine it. Learn to extract actionable insights from massive, complex datasets.
Core Curriculum: Statistical mathematics, probability, and exploratory data analysis using Python (NumPy, pandas, Matplotlib).
Machine Learning: Implementing predictive models using scikit-learn, covering regression, classification, clustering, and ensemble methods.
Advanced Topics: Introduction to deep learning, natural language processing (NLP), and data visualization tools like Tableau or Power BI.

8. Generative AI
Step into the future of technology with our Generative AI program. This is for developers who want to build the next generation of intelligent applications.
Core Curriculum: Understanding Large Language Models (LLMs), transformer architectures, and embedding spaces.
Applied AI: Prompt engineering, fine-tuning open-source models (like Llama or Mistral), and building RAG (Retrieval-Augmented Generation) pipelines.
Frameworks: Hands-on experience with LangChain, LlamaIndex, vector databases (Pinecone, Milvus), and integrating AI agents into existing software.

9. Cyber Security with AI
As cyber threats grow more sophisticated, traditional defense mechanisms are no longer enough. This course combines ethical hacking with artificial intelligence.
Core Curriculum: Network security, cryptography, vulnerability assessment, and penetration testing methodologies.
AI Integration: Using machine learning algorithms for anomaly detection, automated threat hunting, and behavioral analysis.
Outcomes: You will learn to secure enterprise networks, conduct ethical hacks, and build AI-driven defense systems that adapt to zero-day vulnerabilities.

Business & Strategy

10. Digital Marketing
Great products need great visibility. This course turns you into a digital growth engine, combining creative strategy with analytical rigor.
Core Curriculum: Search Engine Optimization (SEO), Search Engine Marketing (SEM), and content marketing strategies.
Campaign Management: Mastery of Google Ads, Meta Ads (Facebook/Instagram), and email marketing automation.
Analytics & Optimization: Using Google Analytics to track user behavior, A/B testing, and Conversion Rate Optimization (CRO) to maximize ROI.

Why Choose Amal Tej Academy?

With over 6 years of educational excellence, AT Academy isn't just about handing out certificates. We focus on building real-world competence.

Industry-Veteran Instructors: Learn from professionals who have spent years in the trenches of top tech companies.
Project-Based Learning: Every course requires the completion of live, industry-grade projects that you can showcase in your portfolio.
Comprehensive Placement Support: We offer resume building, mock interviews, and dedicated career guidance to ensure our graduates land their dream jobs.

Technology doesn't wait, and neither should you. Whether you want to design the next microchip, build scalable cloud architectures, or pioneer Generative AI, AT Academy has the roadmap for your success.

Enroll today and build the future with Amal Tej Academy!"""

        blog, created = Blog.objects.update_or_create(
            slug=slug,
            defaults={
                'title': 'Welcome to AT Academy: Empowering Tech Leaders for Over 6 Years',
                'category': 'general',
                'content': content,
                'meta_title': 'Welcome to AT Academy | Empowering Tech Leaders for Over 6 Years',
                'meta_description': 'Discover AT Academy — 6+ years of empowering tech leaders with industry-grade courses in Embedded Systems, VLSI, Full Stack Development, Data Science, AI, and more.',
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'Created blog: {blog.title}'))
        else:
            self.stdout.write(self.style.WARNING(f'Updated blog: {blog.title}'))
