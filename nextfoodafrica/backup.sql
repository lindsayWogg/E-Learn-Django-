pg_dump: warning: there are circular foreign-key constraints on this table:
pg_dump: detail: posts_category
pg_dump: hint: You might not be able to restore the dump without using --disable-triggers or temporarily dropping the constraints.
pg_dump: hint: Consider using a full dump instead of a --data-only dump to avoid this problem.
--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1 (Debian 16.1-1.pgdg120+1)
-- Dumped by pg_dump version 16.1 (Debian 16.1-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	posts	cart
8	posts	category
9	posts	maincourse
10	posts	post
11	posts	order
12	posts	curriculam
13	posts	comment
14	posts	boxes_three
15	posts	reviews
16	posts	features
17	posts	faq
18	posts	timing
19	posts	certificate
20	posts	clients
21	posts	video
22	posts	subcat
23	posts	blog
24	posts	tcforblog
25	posts	blankpage
26	posts	promocode
27	posts	offers
28	posts	partenaires
29	posts	formation
30	posts	bientot
31	posts	collabo
32	posts	utilisateur
33	posts	chapitre
34	posts	quizz
35	posts	objectif
36	posts	demande_inscription
37	posts	student_progess
38	posts	souscription_formation
39	posts	paiement
40	posts	question
41	posts	true_answer
42	posts	answer_possible
43	posts	notes
44	posts	video_chap
45	posts	atelier
46	posts	souscription_atelier
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add cart	7	add_cart
26	Can change cart	7	change_cart
27	Can delete cart	7	delete_cart
28	Can view cart	7	view_cart
29	Can add category	8	add_category
30	Can change category	8	change_category
31	Can delete category	8	delete_category
32	Can view category	8	view_category
33	Can add main course	9	add_maincourse
34	Can change main course	9	change_maincourse
35	Can delete main course	9	delete_maincourse
36	Can view main course	9	view_maincourse
37	Can add post	10	add_post
38	Can change post	10	change_post
39	Can delete post	10	delete_post
40	Can view post	10	view_post
41	Can add order	11	add_order
42	Can change order	11	change_order
43	Can delete order	11	delete_order
44	Can view order	11	view_order
45	Can add curriculam	12	add_curriculam
46	Can change curriculam	12	change_curriculam
47	Can delete curriculam	12	delete_curriculam
48	Can view curriculam	12	view_curriculam
49	Can add comment	13	add_comment
50	Can change comment	13	change_comment
51	Can delete comment	13	delete_comment
52	Can view comment	13	view_comment
53	Can add boxes_three	14	add_boxes_three
54	Can change boxes_three	14	change_boxes_three
55	Can delete boxes_three	14	delete_boxes_three
56	Can view boxes_three	14	view_boxes_three
57	Can add reviews	15	add_reviews
58	Can change reviews	15	change_reviews
59	Can delete reviews	15	delete_reviews
60	Can view reviews	15	view_reviews
61	Can add features	16	add_features
62	Can change features	16	change_features
63	Can delete features	16	delete_features
64	Can view features	16	view_features
65	Can add faq	17	add_faq
66	Can change faq	17	change_faq
67	Can delete faq	17	delete_faq
68	Can view faq	17	view_faq
69	Can add timing	18	add_timing
70	Can change timing	18	change_timing
71	Can delete timing	18	delete_timing
72	Can view timing	18	view_timing
73	Can add certificate	19	add_certificate
74	Can change certificate	19	change_certificate
75	Can delete certificate	19	delete_certificate
76	Can view certificate	19	view_certificate
77	Can add clients	20	add_clients
78	Can change clients	20	change_clients
79	Can delete clients	20	delete_clients
80	Can view clients	20	view_clients
81	Can add video	21	add_video
82	Can change video	21	change_video
83	Can delete video	21	delete_video
84	Can view video	21	view_video
85	Can add subcat	22	add_subcat
86	Can change subcat	22	change_subcat
87	Can delete subcat	22	delete_subcat
88	Can view subcat	22	view_subcat
89	Can add blog	23	add_blog
90	Can change blog	23	change_blog
91	Can delete blog	23	delete_blog
92	Can view blog	23	view_blog
93	Can add tcforblog	24	add_tcforblog
94	Can change tcforblog	24	change_tcforblog
95	Can delete tcforblog	24	delete_tcforblog
96	Can view tcforblog	24	view_tcforblog
97	Can add blankpage	25	add_blankpage
98	Can change blankpage	25	change_blankpage
99	Can delete blankpage	25	delete_blankpage
100	Can view blankpage	25	view_blankpage
101	Can add promocode	26	add_promocode
102	Can change promocode	26	change_promocode
103	Can delete promocode	26	delete_promocode
104	Can view promocode	26	view_promocode
105	Can add offers	27	add_offers
106	Can change offers	27	change_offers
107	Can delete offers	27	delete_offers
108	Can view offers	27	view_offers
109	Can add partenaires	28	add_partenaires
110	Can change partenaires	28	change_partenaires
111	Can delete partenaires	28	delete_partenaires
112	Can view partenaires	28	view_partenaires
113	Can add formation	29	add_formation
114	Can change formation	29	change_formation
115	Can delete formation	29	delete_formation
116	Can view formation	29	view_formation
117	Can add bientot	30	add_bientot
118	Can change bientot	30	change_bientot
119	Can delete bientot	30	delete_bientot
120	Can view bientot	30	view_bientot
121	Can add collabo	31	add_collabo
122	Can change collabo	31	change_collabo
123	Can delete collabo	31	delete_collabo
124	Can view collabo	31	view_collabo
125	Can add utilisateur	32	add_utilisateur
126	Can change utilisateur	32	change_utilisateur
127	Can delete utilisateur	32	delete_utilisateur
128	Can view utilisateur	32	view_utilisateur
129	Can add chapitre	33	add_chapitre
130	Can change chapitre	33	change_chapitre
131	Can delete chapitre	33	delete_chapitre
132	Can view chapitre	33	view_chapitre
133	Can add quizz	34	add_quizz
134	Can change quizz	34	change_quizz
135	Can delete quizz	34	delete_quizz
136	Can view quizz	34	view_quizz
137	Can add ojectif	35	add_ojectif
138	Can change ojectif	35	change_ojectif
139	Can delete ojectif	35	delete_ojectif
140	Can view ojectif	35	view_ojectif
141	Can add objectif	35	add_objectif
142	Can change objectif	35	change_objectif
143	Can delete objectif	35	delete_objectif
144	Can view objectif	35	view_objectif
145	Can add demande_inscription	36	add_demande_inscription
146	Can change demande_inscription	36	change_demande_inscription
147	Can delete demande_inscription	36	delete_demande_inscription
148	Can view demande_inscription	36	view_demande_inscription
149	Can add student_progess	37	add_student_progess
150	Can change student_progess	37	change_student_progess
151	Can delete student_progess	37	delete_student_progess
152	Can view student_progess	37	view_student_progess
153	Can add souscription_formation	38	add_souscription_formation
154	Can change souscription_formation	38	change_souscription_formation
155	Can delete souscription_formation	38	delete_souscription_formation
156	Can view souscription_formation	38	view_souscription_formation
157	Can add paiement	39	add_paiement
158	Can change paiement	39	change_paiement
159	Can delete paiement	39	delete_paiement
160	Can view paiement	39	view_paiement
161	Can add question	40	add_question
162	Can change question	40	change_question
163	Can delete question	40	delete_question
164	Can view question	40	view_question
165	Can add true_answer	41	add_true_answer
166	Can change true_answer	41	change_true_answer
167	Can delete true_answer	41	delete_true_answer
168	Can view true_answer	41	view_true_answer
169	Can add answer_possible	42	add_answer_possible
170	Can change answer_possible	42	change_answer_possible
171	Can delete answer_possible	42	delete_answer_possible
172	Can view answer_possible	42	view_answer_possible
173	Can add notes	43	add_notes
174	Can change notes	43	change_notes
175	Can delete notes	43	delete_notes
176	Can view notes	43	view_notes
177	Can add video_chap	44	add_video_chap
178	Can change video_chap	44	change_video_chap
179	Can delete video_chap	44	delete_video_chap
180	Can view video_chap	44	view_video_chap
181	Can add atelier	45	add_atelier
182	Can change atelier	45	change_atelier
183	Can delete atelier	45	delete_atelier
184	Can view atelier	45	view_atelier
185	Can add souscription_atelier	46	add_souscription_atelier
186	Can change souscription_atelier	46	change_souscription_atelier
187	Can delete souscription_atelier	46	delete_souscription_atelier
188	Can view souscription_atelier	46	view_souscription_atelier
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
2	pbkdf2_sha256$180000$SEPwO4aWl6XT$kK2GTfMOXSCdzooztoHPVaFdILrcCv1waO2B87/zTB8=	2024-09-28 08:55:35.915459+00	t	admin	admin	admin	admin@gmail.com	f	t	2024-02-12 18:23:56.884583+00
4	pbkdf2_sha256$180000$QZkcqJmWxIRf$NtLO7d8m+Z4wCoGCHWcjzgoi3lPyt8hZdTgmcgOGqSc=	2024-10-05 07:19:00.962209+00	f	wogg	Andriamanantena	Lindsay Wogg	newsolomail@gmail.com	f	t	2024-02-17 07:02:39.146877+00
17	pbkdf2_sha256$180000$YCZsYozzHpXQ$Hj18JlpL6IUYR/eIy+rdtsLpqKnQequAmiq4F+WWRMg=	2024-08-24 14:18:01.628255+00	f	thierry	Thierry	Andriamanantena	thierry@gmail.com	f	t	2024-03-30 17:06:12.519995+00
18	pbkdf2_sha256$180000$tkG5bFgapcqw$U8rNqUah+iP8GsALAhAE0qO2vZVBnXJWqQv6yHPXXdY=	2024-08-31 13:37:55.012474+00	f	fanja	Annissah	Fanjatiana	fanjatiana@gmail.com	f	t	2024-03-30 17:25:20.80193+00
19	pbkdf2_sha256$180000$RJfP4VwoivCm$vaDFJzbT/SQ80i/cpd1LFu0ZWQk5Pn/mksuouJd8UL8=	\N	f	toky45	Rojovola	Rakotomamonjy	toky45@gmail.com	f	t	2024-09-07 09:05:07.849472+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2024-02-10 06:07:15.976763+00
2	auth	0001_initial	2024-02-10 06:07:16.071728+00
3	admin	0001_initial	2024-02-10 06:07:16.100096+00
4	admin	0002_logentry_remove_auto_add	2024-02-10 06:07:16.113475+00
5	admin	0003_logentry_add_action_flag_choices	2024-02-10 06:07:16.13057+00
6	contenttypes	0002_remove_content_type_name	2024-02-10 06:07:16.167052+00
7	auth	0002_alter_permission_name_max_length	2024-02-10 06:07:16.192596+00
8	auth	0003_alter_user_email_max_length	2024-02-10 06:07:16.210185+00
9	auth	0004_alter_user_username_opts	2024-02-10 06:07:16.224746+00
10	auth	0005_alter_user_last_login_null	2024-02-10 06:07:16.242215+00
11	auth	0006_require_contenttypes_0002	2024-02-10 06:07:16.24569+00
12	auth	0007_alter_validators_add_error_messages	2024-02-10 06:07:16.265541+00
13	auth	0008_alter_user_username_max_length	2024-02-10 06:07:16.290813+00
14	auth	0009_alter_user_last_name_max_length	2024-02-10 06:07:16.309842+00
15	auth	0010_alter_group_name_max_length	2024-02-10 06:07:16.331619+00
16	auth	0011_update_proxy_permissions	2024-02-10 06:07:16.356427+00
17	auth	0012_alter_user_first_name_max_length	2024-02-10 06:07:16.375088+00
18	posts	0001_initial	2024-02-10 06:07:16.650074+00
19	posts	0002_auto_20201216_1940	2024-02-10 06:07:16.665488+00
20	posts	0003_auto_20201217_1117	2024-02-10 06:07:16.696556+00
21	posts	0004_auto_20201217_1810	2024-02-10 06:07:16.729679+00
22	posts	0005_reviews	2024-02-10 06:07:16.792008+00
23	posts	0006_features	2024-02-10 06:07:16.83615+00
24	posts	0007_faq_timing	2024-02-10 06:07:16.918524+00
25	posts	0008_delete_timing	2024-02-10 06:07:16.922455+00
26	posts	0009_certificate_timing	2024-02-10 06:07:17.058782+00
27	posts	0010_auto_20201218_1508	2024-02-10 06:07:17.096925+00
28	posts	0011_auto_20201218_1556	2024-02-10 06:07:17.123445+00
29	posts	0012_cart_certificate	2024-02-10 06:07:17.15559+00
30	posts	0013_post_file	2024-02-10 06:07:17.179099+00
31	posts	0014_auto_20201219_1148	2024-02-10 06:07:17.255699+00
32	posts	0015_order_certificate	2024-02-10 06:07:17.279791+00
33	posts	0016_remove_order_certificate	2024-02-10 06:07:17.310275+00
34	posts	0017_auto_20201219_1312	2024-02-10 06:07:17.38156+00
35	posts	0018_auto_20201219_1313	2024-02-10 06:07:17.473329+00
36	posts	0019_auto_20201219_1515	2024-02-10 06:07:17.538766+00
37	posts	0020_auto_20201221_1337	2024-02-10 06:07:17.595843+00
38	posts	0021_auto_20201221_1338	2024-02-10 06:07:17.722824+00
39	posts	0022_video	2024-02-10 06:07:17.769466+00
40	posts	0023_auto_20210104_1057	2024-02-10 06:07:17.849642+00
41	posts	0024_subcat	2024-02-10 06:07:17.900296+00
42	posts	0025_post_subcategory	2024-02-10 06:07:17.943837+00
43	posts	0026_auto_20210104_1751	2024-02-10 06:07:17.978573+00
44	posts	0027_category_more	2024-02-10 06:07:17.993958+00
45	posts	0028_auto_20210105_1105	2024-02-10 06:07:18.180849+00
46	posts	0029_auto_20210105_1534	2024-02-10 06:07:18.258031+00
47	posts	0030_category_logo	2024-02-10 06:07:18.2693+00
48	posts	0031_auto_20210105_1605	2024-02-10 06:07:18.283373+00
49	posts	0032_auto_20210105_1643	2024-02-10 06:07:18.343934+00
50	posts	0033_auto_20210106_1032	2024-02-10 06:07:18.385135+00
51	posts	0034_auto_20210106_1040	2024-02-10 06:07:18.435272+00
52	posts	0035_auto_20210106_1327	2024-02-10 06:07:18.504826+00
53	posts	0036_auto_20210106_1334	2024-02-10 06:07:18.620478+00
54	posts	0037_auto_20210106_1344	2024-02-10 06:07:18.734852+00
55	posts	0038_auto_20210106_1743	2024-02-10 06:07:18.798452+00
56	posts	0039_auto_20210108_1536	2024-02-10 06:07:18.858808+00
57	posts	0040_order_coupon	2024-02-10 06:07:18.904167+00
58	posts	0041_auto_20210108_1718	2024-02-10 06:07:18.917405+00
59	posts	0042_auto_20210108_1744	2024-02-10 06:07:18.926566+00
60	posts	0043_auto_20210108_1746	2024-02-10 06:07:18.985254+00
61	posts	0044_auto_20210108_1748	2024-02-10 06:07:19.034678+00
62	posts	0045_category_disc	2024-02-10 06:07:19.05689+00
63	posts	0046_auto_20210112_1545	2024-02-10 06:07:19.145028+00
64	posts	0047_auto_20210112_1921	2024-02-10 06:07:19.172883+00
65	posts	0048_auto_20210112_1922	2024-02-10 06:07:19.382748+00
66	posts	0049_category_hit	2024-02-10 06:07:19.397979+00
67	posts	0050_auto_20210113_1613	2024-02-10 06:07:19.413492+00
68	posts	0051_auto_20210113_1614	2024-02-10 06:07:19.515075+00
69	posts	0052_auto_20210114_1112	2024-02-10 06:07:19.544895+00
70	posts	0053_auto_20210122_1318	2024-02-10 06:07:19.885073+00
71	posts	0054_auto_20210122_1628	2024-02-10 06:07:20.194402+00
72	posts	0055_auto_20210122_1659	2024-02-10 06:07:20.238231+00
73	posts	0056_message	2024-02-10 06:07:20.246905+00
74	posts	0057_auto_20210210_1041	2024-02-10 06:07:20.303901+00
75	posts	0058_auto_20210216_1717	2024-02-10 06:07:20.347219+00
76	posts	0059_offers_active	2024-02-10 06:07:20.353862+00
77	posts	0060_offers_button_url	2024-02-10 06:07:20.361316+00
78	posts	0061_delete_message	2024-02-10 06:07:20.366929+00
79	posts	0062_partenaires	2024-02-10 06:07:20.375661+00
80	posts	0063_auto_20231223_1448	2024-02-10 06:07:20.388281+00
81	posts	0064_partenaires_partner_id	2024-02-10 06:07:20.395131+00
82	posts	0065_partenaires_description	2024-02-10 06:07:20.40863+00
83	posts	0066_formation	2024-02-10 06:07:20.418683+00
84	posts	0067_formation_foormation_img	2024-02-10 06:07:20.428816+00
85	posts	0068_auto_20231230_1416	2024-02-10 06:07:20.446888+00
86	posts	0069_bientot_prog_img	2024-02-10 06:07:20.458745+00
87	posts	0070_collabo	2024-02-10 06:07:20.470771+00
88	posts	0071_collabo_post	2024-02-10 06:07:20.482411+00
89	posts	0072_message	2024-02-10 06:07:20.493547+00
90	posts	0073_message_date	2024-02-10 06:07:20.506259+00
91	posts	0074_auto_20231230_1901	2024-02-10 06:07:20.513563+00
92	posts	0075_auto_20231230_1904	2024-02-10 06:07:20.531388+00
93	posts	0076_auto_20231230_1906	2024-02-10 06:07:20.544308+00
94	posts	0077_auto_20231230_1906	2024-02-10 06:07:20.561623+00
95	posts	0078_remove_message_datemessage	2024-02-10 06:07:20.567457+00
96	posts	0079_message_date	2024-02-10 06:07:20.625896+00
110	posts	0093_alter_bientot_id_alter_blankpage_id_alter_blog_id_and_more	2024-02-10 06:07:21.894706+00
111	sessions	0001_initial	2024-02-10 06:07:21.932544+00
112	posts	0094_utilisateur_profile_pic	2024-02-10 07:28:58.888825+00
118	posts	0080_remove_message_date	2024-02-13 18:01:57.659245+00
119	posts	0081_message_date	2024-02-13 18:01:57.671964+00
120	posts	0082_auto_20231230_1923	2024-02-13 18:01:57.679399+00
121	posts	0083_auto_20231230_1924	2024-02-13 18:01:57.69088+00
122	posts	0084_delete_message	2024-02-13 18:01:57.698318+00
123	posts	0085_appprenant	2024-02-13 18:01:57.714467+00
124	posts	0086_auto_20240120_1435	2024-02-13 18:01:57.788304+00
125	posts	0087_auto_20240120_1443	2024-02-13 18:01:57.882645+00
126	posts	0088_delete_customer	2024-02-13 18:01:57.888802+00
127	posts	0089_auto_20240120_1447	2024-02-13 18:01:57.904094+00
128	posts	0090_auto_20240120_1718	2024-02-13 18:01:57.922766+00
129	posts	0091_auto_20240203_1454	2024-02-13 18:01:57.993147+00
130	posts	0092_formation_formation_type	2024-02-13 18:01:58.001574+00
131	posts	0093_auto_20240210_1707	2024-02-13 18:01:58.035567+00
132	posts	0094_remove_quizz_status	2024-02-13 18:01:58.044696+00
133	posts	0095_quizz_status	2024-02-13 18:01:58.053266+00
134	posts	0096_chapitre_titre	2024-02-13 18:01:58.066537+00
135	posts	0097_utilisateur_user_type	2024-02-13 18:01:58.078667+00
136	posts	0098_remove_utilisateur_email	2024-02-13 18:04:25.950636+00
137	posts	0099_utilisateur_email	2024-02-13 18:04:25.958975+00
138	posts	0100_utilisateur_matricule	2024-02-13 18:11:55.407318+00
139	posts	0093_auto_20240217_1251	2024-02-17 07:29:36.419734+00
140	posts	0094_auto_20240217_1436	2024-02-17 09:06:27.662098+00
141	posts	0095_chapitre_duree_min	2024-02-17 12:13:54.236758+00
142	posts	0096_remove_chapitre_objectif	2024-02-17 12:28:47.122849+00
143	posts	0097_ojectif	2024-02-17 12:29:38.318963+00
144	posts	0098_ojectif_duree_min	2024-02-17 12:32:33.152267+00
145	posts	0099_auto_20240217_1817	2024-02-17 12:47:28.430965+00
146	posts	0100_chapitre_description	2024-02-17 13:00:57.728356+00
147	posts	0101_auto_20240217_1832	2024-02-17 13:02:07.588886+00
148	posts	0101_auto_20240224_1324	2024-02-24 07:55:20.646327+00
149	posts	0102_auto_20240224_1329	2024-02-24 08:00:36.337188+00
150	posts	0103_auto_20240224_1330	2024-02-24 08:00:51.306932+00
151	posts	0104_formation_created_at	2024-02-24 09:44:29.801291+00
152	posts	0105_auto_20240224_1738	2024-02-24 12:08:36.896291+00
153	posts	0106_auto_20240224_1759	2024-02-24 12:29:31.560392+00
154	posts	0107_auto_20240224_1939	2024-02-24 14:09:26.806602+00
155	posts	0108_auto_20240229_1220	2024-02-29 06:50:30.192905+00
156	posts	0109_auto_20240229_1225	2024-02-29 06:55:35.668139+00
157	posts	0110_auto_20240229_1227	2024-02-29 06:57:37.197386+00
158	posts	0111_chapitre_chap_order	2024-02-29 08:01:36.576483+00
159	posts	0112_auto_20240302_1731	2024-03-02 12:01:18.069487+00
160	posts	0113_auto_20240302_1732	2024-03-02 12:03:00.302653+00
161	posts	0114_formation_formation_duree	2024-03-02 14:30:03.372851+00
162	posts	0115_auto_20240312_0031	2024-03-11 19:01:15.97618+00
195	posts	0116_auto_20240316_1406	2024-03-16 08:36:50.623243+00
196	posts	0117_auto_20240316_1850	2024-03-16 13:20:21.683338+00
197	posts	0118_auto_20240330_1419	2024-03-30 08:49:58.802361+00
198	posts	0119_utilisateur_id	2024-03-30 09:02:09.054507+00
199	posts	0120_remove_utilisateur_id	2024-03-30 09:32:59.486746+00
200	posts	0121_utilisateur_date_souscription	2024-03-30 10:35:12.4423+00
201	posts	0122_demande_inscription_date_validation	2024-03-30 10:45:29.797523+00
202	posts	0123_remove_demande_inscription_date_validation	2024-03-30 10:45:29.80135+00
203	posts	0124_demande_inscription_date_validation	2024-03-30 10:46:44.599996+00
204	posts	0125_auto_20240330_2013	2024-03-30 14:43:25.119614+00
205	posts	0126_auto_20240406_1558	2024-04-06 10:28:58.255986+00
206	posts	0127_auto_20240406_1618	2024-04-06 10:56:46.318583+00
207	posts	0128_auto_20240406_1624	2024-04-06 10:56:46.356556+00
208	posts	0129_auto_20240406_1629	2024-04-06 10:59:56.178348+00
209	posts	0130_auto_20240406_1647	2024-04-06 11:18:56.433495+00
210	posts	0131_paiement	2024-04-06 15:11:03.467276+00
211	posts	0132_paiement_matricule	2024-04-06 17:38:38.955252+00
212	posts	0133_auto_20240406_2318	2024-04-06 17:48:56.48119+00
213	posts	0134_paiement_date_paiemnet	2024-04-06 18:01:30.826426+00
214	posts	0135_auto_20240406_2333	2024-04-06 18:03:32.037498+00
215	posts	0136_auto_20240413_1812	2024-04-13 12:42:29.86474+00
216	posts	0137_auto_20240420_2009	2024-04-20 14:39:20.000564+00
217	posts	0138_question_chap_id	2024-04-20 16:42:35.415865+00
218	posts	0139_auto_20240427_1526	2024-04-27 10:02:57.215467+00
219	posts	0140_auto_20240427_1615	2024-04-27 10:45:53.518335+00
220	posts	0141_auto_20240427_1704	2024-04-27 11:34:38.520048+00
221	posts	0142_auto_20240504_1448	2024-05-04 09:18:16.869578+00
222	posts	0143_auto_20240504_1519	2024-05-04 09:49:58.580129+00
223	posts	0144_auto_20240511_1344	2024-05-11 08:14:35.235614+00
224	posts	0145_auto_20240525_1456	2024-05-25 09:26:48.193252+00
225	posts	0146_auto_20240601_1851	2024-06-01 13:21:59.532941+00
226	posts	0147_auto_20240615_1922	2024-06-15 13:53:00.205335+00
227	posts	0148_formation_formation_presentation	2024-06-15 14:46:30.351193+00
228	posts	0149_auto_20240622_1330	2024-06-22 08:00:26.482313+00
229	posts	0150_auto_20240622_1418	2024-06-22 08:49:00.512621+00
230	posts	0151_auto_20240706_1336	2024-07-06 08:09:25.96328+00
231	posts	0152_auto_20240706_1404	2024-07-06 08:34:40.22646+00
232	posts	0153_auto_20240706_1512	2024-07-06 09:42:27.502484+00
233	posts	0154_auto_20240706_1604	2024-07-06 10:34:51.621012+00
234	posts	0155_auto_20240706_1626	2024-07-06 10:56:10.92005+00
235	posts	0156_auto_20240706_1626	2024-07-06 11:01:59.341258+00
236	posts	0157_auto_20240803_1427	2024-08-03 08:57:59.141808+00
237	posts	0158_auto_20240803_1519	2024-08-03 09:49:32.560359+00
238	posts	0159_auto_20240815_2114	2024-08-15 15:44:15.227082+00
239	posts	0160_auto_20240928_1919	2024-09-28 13:49:39.244099+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
0sjcc5sbplo24ivi0ql1hu7ivnj27uhu	.eJxVjMsOwiAQRf-FtSEDLTC4dO83kOExUjU0Ke3K-O_apAvd3nPOfYlA21rD1ssSpizOQonT7xYpPUrbQb5Tu80yzW1dpih3RR60y-ucy_NyuH8HlXr91mQJi0NFedSRkwM0evTIxOwVFGNVMhRh8MwWEDQlMzhWEREAMBvx_gDqQjeh:1rYgbQ:miGVOUSKG2UBdXWPG_LFOsnIojiOmeWW4MDxzzPdoGc	2024-02-24 06:12:40.20346+00
ubbss92ca1jp2pozpt0exs0mu7csnbgb	NDYzNzcyNGI3NGZjODdjNTRhOWJkYTE3NjFlNDczMDJiMjdiYmYxNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4MmIzOThiNDc3ZTljMGEwNzg2NTljMmE0ZThjZTlmMzhlNDlhZjJiIn0=	2024-02-24 11:41:06.185349+00
sevfpd0y90ylphdzo46v0tzxfiaghd3h	NmU1OTcwMTliZWEzZTFiYmZkYTgwZjFhZDIxOTI5NWZmMDRiYTU1MTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOTRiOTBmYWE5MmY3NTZkM2E5MGJlM2JiZWY1NzgxOTAzM2MxNGNlIn0=	2024-02-26 18:38:56.749632+00
8xq0t3y54bg3t3rqof4b0bpm3l5sp85g	NmFjMzA1NGZiMGMxZGUyM2NjZDk0YzJiMDg1NTQ5NTE3Yzk4NTRkOTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkNTUyMDMzZmQ4ODExNDA1ZjI1OWMwMWEzZjNlN2I4NzllOTAyYzdjIn0=	2024-03-02 08:33:31.532745+00
l4p9lxmrhssccy0mfhh9o0txayzrqcpw	NmFjMzA1NGZiMGMxZGUyM2NjZDk0YzJiMDg1NTQ5NTE3Yzk4NTRkOTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkNTUyMDMzZmQ4ODExNDA1ZjI1OWMwMWEzZjNlN2I4NzllOTAyYzdjIn0=	2024-03-02 09:39:15.750024+00
y6ystxutzw9ng2go22yczkwpbi3z88jf	NmU1OTcwMTliZWEzZTFiYmZkYTgwZjFhZDIxOTI5NWZmMDRiYTU1MTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOTRiOTBmYWE5MmY3NTZkM2E5MGJlM2JiZWY1NzgxOTAzM2MxNGNlIn0=	2024-03-02 14:34:42.84575+00
fgw7o6dbbhbrqrxgj057002lgq1h5vnd	NmU1OTcwMTliZWEzZTFiYmZkYTgwZjFhZDIxOTI5NWZmMDRiYTU1MTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOTRiOTBmYWE5MmY3NTZkM2E5MGJlM2JiZWY1NzgxOTAzM2MxNGNlIn0=	2024-03-09 08:14:54.130063+00
80ih1bd57i71kb6xna8r01eoxhpplvdf	NmU1OTcwMTliZWEzZTFiYmZkYTgwZjFhZDIxOTI5NWZmMDRiYTU1MTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOTRiOTBmYWE5MmY3NTZkM2E5MGJlM2JiZWY1NzgxOTAzM2MxNGNlIn0=	2024-03-14 02:42:51.347178+00
ltoa376268qjhp4hx8202ylyw0xsktfh	NmU1OTcwMTliZWEzZTFiYmZkYTgwZjFhZDIxOTI5NWZmMDRiYTU1MTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOTRiOTBmYWE5MmY3NTZkM2E5MGJlM2JiZWY1NzgxOTAzM2MxNGNlIn0=	2024-03-16 06:33:28.4619+00
iqle2t5vbkzpwu1x0teberp608jxt40t	NmU1OTcwMTliZWEzZTFiYmZkYTgwZjFhZDIxOTI5NWZmMDRiYTU1MTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOTRiOTBmYWE5MmY3NTZkM2E5MGJlM2JiZWY1NzgxOTAzM2MxNGNlIn0=	2024-03-16 08:22:37.888946+00
lnfjc22fsxzppqkh83c4ur1roegcvaih	NmU1OTcwMTliZWEzZTFiYmZkYTgwZjFhZDIxOTI5NWZmMDRiYTU1MTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOTRiOTBmYWE5MmY3NTZkM2E5MGJlM2JiZWY1NzgxOTAzM2MxNGNlIn0=	2024-03-16 08:25:57.9978+00
g7ibm3pacuhn7iqyaotr95zwayr9396j	NmU1OTcwMTliZWEzZTFiYmZkYTgwZjFhZDIxOTI5NWZmMDRiYTU1MTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOTRiOTBmYWE5MmY3NTZkM2E5MGJlM2JiZWY1NzgxOTAzM2MxNGNlIn0=	2024-03-18 17:38:24.686343+00
t7uwfjeakh824gtkn51xm0qlm8w6m41z	ZTU3YThiMGFkMzExNzg5NDgyMTljYzI5YTk4MWExNjJhMzVhZDA3ZDp7Il9tZXNzYWdlcyI6IltbXCJfX2pzb25fbWVzc2FnZVwiLDAsMjUsXCI8Yj5GXFx1MDBlOWxpY2l0YXRpb24hISEgVm90cmUgZGUgbWFuZGUgZCdpbnNjcmlwdGlvbiBhIGJpZW4gXFx1MDBlOXRcXHUwMGU5IGVucmVnaXN0clxcdTAwZTkhPC9iPiA8YnI+Vm91cyBzZXJleiBub3RpZmlcXHUwMGU5IHBhciBFLW1haWwgYXByXFx1MDBlOHMgbGEgdmFsaWRhdGlvbiBkZSB2b3RyZSBkZW1hbmRlLlwiXV0ifQ==	2024-03-29 04:02:09.522431+00
q1bx9y6v1sf9jajdy9l9lxoywg9ud789	NmFjMzA1NGZiMGMxZGUyM2NjZDk0YzJiMDg1NTQ5NTE3Yzk4NTRkOTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkNTUyMDMzZmQ4ODExNDA1ZjI1OWMwMWEzZjNlN2I4NzllOTAyYzdjIn0=	2024-03-30 11:10:08.459307+00
p1j4q52q25nvfshiterpudvjg3szwfwq	NmU1OTcwMTliZWEzZTFiYmZkYTgwZjFhZDIxOTI5NWZmMDRiYTU1MTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOTRiOTBmYWE5MmY3NTZkM2E5MGJlM2JiZWY1NzgxOTAzM2MxNGNlIn0=	2024-04-15 06:36:22.804766+00
xoegu3vxmt8spv2gs966bx1v84xlu7h0	NmU1OTcwMTliZWEzZTFiYmZkYTgwZjFhZDIxOTI5NWZmMDRiYTU1MTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOTRiOTBmYWE5MmY3NTZkM2E5MGJlM2JiZWY1NzgxOTAzM2MxNGNlIn0=	2024-04-15 16:05:16.610074+00
6epo8aum299ryi8j5cs0ucv0s2i3tiij	NmU1OTcwMTliZWEzZTFiYmZkYTgwZjFhZDIxOTI5NWZmMDRiYTU1MTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOTRiOTBmYWE5MmY3NTZkM2E5MGJlM2JiZWY1NzgxOTAzM2MxNGNlIn0=	2024-04-15 16:18:08.750628+00
otcuhvxrs1pkzz7qula5ft89ycnvj3im	NmU1OTcwMTliZWEzZTFiYmZkYTgwZjFhZDIxOTI5NWZmMDRiYTU1MTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOTRiOTBmYWE5MmY3NTZkM2E5MGJlM2JiZWY1NzgxOTAzM2MxNGNlIn0=	2024-04-15 18:02:48.49902+00
kpj2z4ej5tp5jlcdme73yzybooffzg12	NmU1OTcwMTliZWEzZTFiYmZkYTgwZjFhZDIxOTI5NWZmMDRiYTU1MTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOTRiOTBmYWE5MmY3NTZkM2E5MGJlM2JiZWY1NzgxOTAzM2MxNGNlIn0=	2024-05-11 08:47:18.138517+00
2xi358y989g5ud51js4vn1loxxf16oyi	ODQ4MDcxYjQwNGFhNDM4NWVhNDM3YTdhZmFjMTc3M2QzNDFlNGNjNDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZjViNjBjNjEwNjNjODc4ZjA3NmU4YWYyNWVkODg2N2MzNTliZDAwIn0=	2024-07-13 06:32:49.075376+00
degq4tyqedy68bqjyvkm50y5x8lap9ww	NmU1OTcwMTliZWEzZTFiYmZkYTgwZjFhZDIxOTI5NWZmMDRiYTU1MTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOTRiOTBmYWE5MmY3NTZkM2E5MGJlM2JiZWY1NzgxOTAzM2MxNGNlIn0=	2024-08-10 08:02:50.691444+00
duxmatec1b71xd0xutl8aejd70gdvd6h	ODQ4MDcxYjQwNGFhNDM4NWVhNDM3YTdhZmFjMTc3M2QzNDFlNGNjNDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZjViNjBjNjEwNjNjODc4ZjA3NmU4YWYyNWVkODg2N2MzNTliZDAwIn0=	2024-08-10 08:14:16.996737+00
d0w558rcc2muves8wepqp7e9cpnyjhlt	NmU1OTcwMTliZWEzZTFiYmZkYTgwZjFhZDIxOTI5NWZmMDRiYTU1MTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOTRiOTBmYWE5MmY3NTZkM2E5MGJlM2JiZWY1NzgxOTAzM2MxNGNlIn0=	2024-08-10 08:21:35.392868+00
36oa3zbj57md96zfl5q17ghepk325ocz	ODQ4MDcxYjQwNGFhNDM4NWVhNDM3YTdhZmFjMTc3M2QzNDFlNGNjNDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZjViNjBjNjEwNjNjODc4ZjA3NmU4YWYyNWVkODg2N2MzNTliZDAwIn0=	2024-09-26 18:50:48.571676+00
s4xymc0nep6ph49fywlm9fbqd5mnp5qf	NmU1OTcwMTliZWEzZTFiYmZkYTgwZjFhZDIxOTI5NWZmMDRiYTU1MTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOTRiOTBmYWE5MmY3NTZkM2E5MGJlM2JiZWY1NzgxOTAzM2MxNGNlIn0=	2024-09-28 07:57:04.074358+00
bqbjw2tw7qd4said9age6nsy5x1d9mst	ODQ4MDcxYjQwNGFhNDM4NWVhNDM3YTdhZmFjMTc3M2QzNDFlNGNjNDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZjViNjBjNjEwNjNjODc4ZjA3NmU4YWYyNWVkODg2N2MzNTliZDAwIn0=	2024-10-05 07:01:31.316031+00
y5k1mb0faxer99sdd5q230iwvydgz2gp	NmU1OTcwMTliZWEzZTFiYmZkYTgwZjFhZDIxOTI5NWZmMDRiYTU1MTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOTRiOTBmYWE5MmY3NTZkM2E5MGJlM2JiZWY1NzgxOTAzM2MxNGNlIn0=	2024-10-12 08:55:36.14352+00
m0cs5y9psuvlwch24myyjrytjf1j8gqe	ODQ4MDcxYjQwNGFhNDM4NWVhNDM3YTdhZmFjMTc3M2QzNDFlNGNjNDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZjViNjBjNjEwNjNjODc4ZjA3NmU4YWYyNWVkODg2N2MzNTliZDAwIn0=	2024-10-19 07:19:00.969412+00
\.


--
-- Data for Name: posts_chapitre; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_chapitre (chap_id, frmt_id, titre, cours_content, cours_file_type, exemple_content, exemple_file_type, duree_min, description, date_creation, chap_order, quizz_content, quizz_file_type) FROM stdin;
1	tendance	Introduction	formations/courses/INTRO.mp4	video	formations/exemples/PARTIE 1 - 1.mp4	video	UNDEFINED	Une petite description de la formation	2024-03-19 19:09:54.455194+00	0	formations/quizz/TEST 1.png	UNKNOWN
2	ab_bar	premier chapitre	formations/courses/INTRO.mp4	video	formations/exemples/PARTIE 1 - 1.mp4	video	UNDEFINED	Ce texte est généré à des fins de remplissage et n'a pas de signification réelle, il est utilisé comme espace réservé dans la mise en page et la conception. Vous pouvez également générer des textes Lorem Ipsum de différentes longueurs en utilisant des générateurs en ligne ou des bibliothèques de programmation.	2024-03-30 11:17:28.070835+00	0	formations/quizz/TEST 1.png	UNKNOWN
3	ab_bar	deuxième chapitre	formations/courses/INTRO.mp4	video	formations/exemples/PARTIE 1 - 1.mp4	video	UNDEFINED	Ce texte est généré à des fins de remplissage et n'a pas de signification réelle, il est utilisé comme espace réservé dans la mise en page et la conception. Vous pouvez également générer des textes Lorem Ipsum de différentes longueurs en utilisant des générateurs en ligne ou des bibliothèques de programmation.	2024-03-30 11:19:26.41513+00	0	formations/quizz/TEST 1.png	UNKNOWN
4	business	chapitre 1	formations/courses/INTRO.mp4	video	formations/exemples/PARTIE 1 - 1.mp4	video	UNDEFINED	Ce texte est généré à des fins de remplissage et n'a pas de signification réelle, il est utilisé comme espace réservé dans la mise en page et la conception. Vous pouvez également générer des textes Lorem Ipsum de différentes longueurs en utilisant des générateurs en ligne ou des bibliothèques de programmation.	2024-04-06 12:19:42.833534+00	0	formations/quizz/TEST 1.png	UNKNOWN
5	business	chapitre 2	formations/courses/INTRO.mp4	video	formations/exemples/PARTIE 1 - 1.mp4	video	UNDEFINED	Ce texte est généré à des fins de remplissage et n'a pas de signification réelle, il est utilisé comme espace réservé dans la mise en page et la conception. Vous pouvez également générer des textes Lorem Ipsum de différentes longueurs en utilisant des générateurs en ligne ou des bibliothèques de programmation.	2024-04-06 12:20:27.095086+00	0	formations/quizz/TEST 1.png	UNKNOWN
6	business	chapitre 2	formations/courses/INTRO.mp4	video	formations/exemples/PARTIE 1 - 1.mp4	video	UNDEFINED	Ce texte est généré à des fins de remplissage et n'a pas de signification réelle, il est utilisé comme espace réservé dans la mise en page et la conception. Vous pouvez également générer des textes Lorem Ipsum de différentes longueurs en utilisant des générateurs en ligne ou des bibliothèques de programmation.	2024-04-06 15:20:15.790788+00	0	formations/quizz/TEST 1.png	UNKNOWN
8	rest_mada	Chapitre 1	formations/presentations/Présentation chap 1.mp4	UNKNOWN	UNUPLOADED	UNKNOWN	UNDEFINED	test du chapitre 1	2024-06-22 08:12:49.648262+00	0	UNUPLOADED	UNKNOWN
9	rest_mada	chapitre 2	formations/presentations/Présentation chap 2.mp4	UNKNOWN	UNUPLOADED	UNKNOWN	UNDEFINED	descr du chapitre 2	2024-06-22 08:13:42.908215+00	0	UNUPLOADED	UNKNOWN
10	rest_mada	chapitre 3	formations/presentations/Présentation chap 3.mp4	UNKNOWN	UNUPLOADED	UNKNOWN	UNDEFINED	descr simple	2024-06-22 08:14:15.086421+00	0	UNUPLOADED	UNKNOWN
11	rest_mada	chapitre 4	formations/presentations/Présentation chap 4.mp4	UNKNOWN	UNUPLOADED	UNKNOWN	UNDEFINED	une simple description	2024-06-22 08:14:45.846271+00	0	UNUPLOADED	UNKNOWN
12	rest_mada	chapitre 5	formations/presentations/Présentation chap 5.mp4	UNKNOWN	UNUPLOADED	UNKNOWN	UNDEFINED	descr du chap 5	2024-06-22 08:15:09.949203+00	0	UNUPLOADED	UNKNOWN
\.


--
-- Data for Name: posts_formation; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_formation (formation_id, formation_name, formation_descr, formation_img, formation_type, formation_prix, created_at, formation_duree, formation_presentation) FROM stdin;
test_form	un simple test	c'est juste un test	blogdesign/assets/img/petr-sevcovic-e5Q5vWO55uU-unsplash.jpg	gratuit	0	2024-06-29	UNDEFINED	formations/presentations/Cha 5 - 2.mp4
form_test	Une formation test	un simple test pour l'accès à des formation payantes	blogdesign/assets/img/POST_FORMATION-EN-LIGNE.jpg	payant	100000	2024-08-03	UNDEFINED	formations/presentations/Screencast from 20.07.2024 17:38:32.webm
info_rest	Informatique dans la restauration	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet, nulla et dictum interdum, nisi lorem egestas odio, vitae scelerisque enim ligula venenatis dolor. Maecenas nisl est, ultrices nec congue eget, auctor vitae massa. Fusce luctus vestibulum augue ut aliquet. Nunc sagittis dictum nisi, sed ullamcorper ipsum dignissim ac. In at libero sed nunc venenatis imperdiet sed ornare turpis. Donec vitae dui eget tellus gravida venenatis. Integer fringilla congue eros non fermentum. Sed dapibus pulvinar nibh tempor porta. Cras ac\r\n	blogdesign/assets/img/jeshoots-com-__ZMnefoI3k-unsplash.jpg	payant	100000	2024-08-31	UNDEFINED	formations/presentations/Titre.mp4
business	Créer son propre business	Créez votre propre business et réaliser le job de vos rêves	blogdesign/assets/img/microsoft-365-oUbzU87d1Gc-unsplash.jpg	payant	100000	2024-03-19	UNDEFINED	formations/presentations/Cha 5 - 2.mp4
BA-ba	BA-ba de l'hygiène alimentaire	Vous découvrirez les aspects les plus importants pour pouvoir mettre en place un plan de nettoyage et de désinfection efficace au sein de votre établissement : les principes de la marche en avant et de HACCP, sécurisation des denrées alimentaires, élaboration d'un plan de nettoyage et de désinfection pertinent.	blogdesign/assets/img/jeshoots-com-__ZMnefoI3k-unsplash.jpg	gratuit	0	2024-03-04	UNDEFINED	formations/presentations/Cha 5 - 2.mp4
tendance	Les tendances en restauration en 2024	Quelles sont les innovations dans le secteur ? Quelles nouveautés vont révolutionner l'Afrique ? Pour vous aider à tirer le meilleur des tendances que nous avons jugées les plus pertinentes pour notre contexte,nous avons conçu ce mini-programme.	blogdesign/assets/img/nick-karvounis-Ciqxn7FE4vE-unsplash.jpg	gratuit	0	2024-03-04	UNDEFINED	formations/presentations/Cha 5 - 2.mp4
ab_bar	Agrandrir son bar	Ce texte est généré à des fins de remplissage et n'a pas de signification réelle, il est utilisé comme espace réservé dans la mise en page et la conception. Vous pouvez également générer des textes Lorem Ipsum de différentes longueurs en utilisant des générateurs en ligne ou des bibliothèques de programmation.	blogdesign/assets/img/bar_formation.jpg	payant	100000	2024-03-19	UNDEFINED	formations/presentations/Cha 5 - 2.mp4
rest_mada	Réussir dans la restauration à Madagascar	Ce mini-programme vous initiera sur les préalables à connaître pour faire de votre restaurant un succès : comment choisir le type de restaurant adapté à votre clientèle, les phases de lancement et de rodage ainsi que les meilleures stratégies de démarrage limitant les risques.	blogdesign/assets/img/petr-sevcovic-e5Q5vWO55uU-unsplash.jpg	gratuit	0	2024-03-04	UNDEFINED	formations/presentations/Cha 5 - 2.mp4
\.


--
-- Data for Name: posts_question; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_question (question_id, question_text, chap_id_id, formation_id_id, answers) FROM stdin;
4	Comment t'appelle tu?	2	ab_bar	{C}
5	c'est qui le chef	2	ab_bar	{A,B,C}
6	où est-tu?	2	ab_bar	{A}
7	que fais tu?	3	ab_bar	{B}
8	qu'est ce que tu veux?	4	business	{B}
9	tu as quelle âge?	4	business	{B}
12		1	tendance	{}
13	comment t'appelle tu?	8	rest_mada	{B}
14	où habite-tu?	8	rest_mada	{A}
15	Quelle âge as-tu?	8	rest_mada	{C}
\.


--
-- Data for Name: posts_answer_possible; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_answer_possible (answer_id, answer_text, question_id_id, answer_alias) FROM stdin;
4	Solo	4	A
5	Jenny	4	B
6	Lindsay	4	C
7	moi	5	A
8	toi	5	B
9	nous	5	C
10	Antananarivo	6	A
11	Antsirabe	6	B
12	Moramange	6	C
13	rien	7	A
14	je dors	7	B
15	je me branle	7	C
16	manger	8	A
17	dormir	8	B
18	boire	8	C
19	1	9	A
20	20	9	B
21	40	9	C
22	tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu	12	A
23		12	B
24		12	C
25	Rindra	13	A
26	Lindsay	13	B
27	Jenny	13	C
28	Anosibe	14	A
29	Andraharo	14	B
30	nullpart	14	C
31	15	15	A
32	78	15	B
33	26	15	C
\.


--
-- Data for Name: posts_atelier; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_atelier (atelier_id, date_creation, date_debut, date_fin, img, description, heure_debut, heure_fin, lieu, titre, price, type, nb_place) FROM stdin;
1	2024-07-06	2024-07-17	2024-07-13	formations/image/petr-sevcovic-e5Q5vWO55uU-unsplash.jpg	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n	09:00	16:00	Ampefiloha	premier atelier	100000	payant	12
4	2024-07-20	2024-07-28	2024-07-29	formations/image/jeshoots-com-__ZMnefoI3k-unsplash.jpg	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n	08:01	17:00	Ampefiloha	Notre atelier	100000	gratuit	12
5	2024-09-14	2024-10-09	2024-10-23	formations/image/petr-sevcovic-e5Q5vWO55uU-unsplash.jpg	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n	08:00	17:00	Anosisoa	Formation NFA	1232345	gratuit	12
6	2024-09-14	2024-08-22	2024-08-23	formations/image/jeshoots-com-__ZMnefoI3k-unsplash.jpg	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n	19:57	15:58	Ampefiloha	Atelier ici	43253425	payant	12
7	2024-09-14	2024-09-15	2024-09-16	formations/image/nick-karvounis-Ciqxn7FE4vE-unsplash.jpg	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n	15:03	22:59	Ampefiloha	Un autre	65575	gratuit	12
\.


--
-- Data for Name: posts_bientot; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_bientot (id, prog_id, prog_title, prog_descr, prog_img, prog_resume) FROM stdin;
2	2	BA-ba de l'hygiène alimentaire	Vous découvrirez les aspects les plus importants pour pouvoir mettre en place un plan de nettoyage et de désinfection efficace au sein de votre établissement : les principes de la marche en avant et de HACCP, sécurisation des denrées alimentaires, élaboration d'un plan de nettoyage et de désinfection pertinent.	blogdesign/assets/img/jeshoots-com-__ZMnefoI3k-unsplash.jpg	resume
1	1	Réussir dans la restauration à Madagascar	Ce mini-programme vous initiera sur les préalables à connaître pour faire de votre restaurant un succès : comment choisir le type de restaurant adapté à votre clientèle, les phases de lancement et de rodage ainsi que les meilleures stratégies de démarrage limitant les risques.	/blogdesign/assets/img/petr-sevcovic-e5Q5vWO55uU-unsplash.jpg	resume
3	3	Les tendances en restauration en 2024	Quelles sont les innovations dans le secteur ? Quelles nouveautés vont révolutionner l'Afrique ? Pour vous aider à tirer le meilleur des tendances que nous avons jugées les plus pertinentes pour notre contexte,nous avons conçu ce mini-programme.	/blogdesign/assets/img/nick-karvounis-Ciqxn7FE4vE-unsplash.jpg	resume
\.


--
-- Data for Name: posts_category; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_category (id, title, slug, top_three_cat, created_at, parent_id, more, logo, disc, hit, logo1, logo2) FROM stdin;
\.


--
-- Data for Name: posts_blankpage; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_blankpage (id, title, meta_tags, meta_desc, slug, image, image_alt_name, "desc", author, date, hit, category_id, disc) FROM stdin;
\.


--
-- Data for Name: posts_blog; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_blog (id, title, meta_tags, meta_desc, slug, image, image_alt_name, "desc", author, date, hit, category_id, disc) FROM stdin;
\.


--
-- Data for Name: posts_boxes_three; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_boxes_three (id, title, slug, category_id) FROM stdin;
\.


--
-- Data for Name: posts_subcat; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_subcat (id, title, slug, created_at, parent_id, disc) FROM stdin;
\.


--
-- Data for Name: posts_post; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_post (id, title, slug, image, logo, "desc", badge, youtube, author, date, hit, button_text, slider_post, price, old_price, discount, emi_start_price, why_title, why1, why2, why3, category_id, meta_desc, meta_tags, file, subcategory_id, image_alt_name, disc) FROM stdin;
\.


--
-- Data for Name: posts_cart; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_cart (id, cart_id, purchase, created, updated, item_id, user_id, certificate) FROM stdin;
\.


--
-- Data for Name: posts_certificate; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_certificate (id, file, created_at, "Post_id") FROM stdin;
\.


--
-- Data for Name: posts_clients; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_clients (id, image) FROM stdin;
\.


--
-- Data for Name: posts_collabo; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_collabo (id, firstname, lastname, sex, date_birth, picture, date_member, post) FROM stdin;
3	Solonirina	Randriamihamina	M	1987-07-26	images/Solo.png	2023-12-01	Tech Lead Senior
2	Jenny	Malala M	F	1989-07-26	images/Jenny.png	2023-12-01	CEO & Hospitality coach
1	Lindsay	Andriamananantena	M	1998-08-28	images/Lindsay.png	2023-12-01	Engineer Data Fullstack
\.


--
-- Data for Name: posts_comment; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_comment (id, name, email, body, created_on, active, post_id, user_id) FROM stdin;
\.


--
-- Data for Name: posts_curriculam; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_curriculam (id, title, content, "Post_id") FROM stdin;
\.


--
-- Data for Name: posts_demande_inscription; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_demande_inscription (dmd_id, matricule, formation_id_id, status, dmd_date, adress, already_signed_up, email, first_name, last_name, password, phone, sex, username, date_validation) FROM stdin;
21	0	ab_bar	validated	2024-03-23	Restaurant KMM	Yes	toky45@gmail.com	Rojovola	Rakotomamonjy	1234AZERTY	0346979370	H	toky45	2024-09-07
\.


--
-- Data for Name: posts_faq; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_faq (id, title, content, "Post_id") FROM stdin;
\.


--
-- Data for Name: posts_features; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_features (id, title, content, "Post_id") FROM stdin;
\.


--
-- Data for Name: posts_maincourse; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_maincourse (id, title, slug, disc) FROM stdin;
\.


--
-- Data for Name: posts_utilisateur; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_utilisateur (password, username, adress, first_name, is_active, is_online, is_staff, last_login, last_name, phone, sex, email, matricule, profile_pic, user_type, date_souscription, activitys, organisation, titre, skype) FROM stdin;
Administration1234	admin	nfa	admin	f	f	f		admin	34565222	H	admin@nf.mg	2	media/profile_pic/default-pic.jpg	admin	2024-03-30				
8D8Tk2r4	thierry	adresse de Thierry	Thierry	t	f	f		Andriamanantena	344343434	H	thierry@gmail.com	17	media/profile_pic/thierry.jpeg	student	2024-03-30				
6w3p8P8I	fanja	Adresse de Fanja	Annissah	t	f	f		Fanjatiana	34543536	F	fanjatiana@gmail.com	18	media/profile_pic/annissah.jpeg	student	2024-03-30	Mon activité dans le food business est déjà performante mais j'aimerais explorer de nouveaux marchés.			
35tcY2L9	toky45	Restaurant KMM	Rojovola	t	f	f		Rakotomamonjy	346979370	H	toky45@gmail.com	19	default-pic.jpg	student	2024-09-07				
Stylo1245	wogg	solo new adress 110	Andriamanantena	f	f	f		Lindsay Wogg	341234567	H	newsolomail@gmail.com	4	media/profile_pic/359959392_677246784046980_3858924738449192981_n (2).jpg	student	2024-03-30	J'ai une idée de Food business mais je n'ai pas encore commencé à l'implémenter.			sololeveling
\.


--
-- Data for Name: posts_notes; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_notes (note_id, note, chap_id_id, formation_id_id, matricule_id) FROM stdin;
3	100	1	tendance	4
2	50	4	business	4
4	0	8	rest_mada	4
\.


--
-- Data for Name: posts_objectif; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_objectif (id, chap_id, frmt_id, objctf_id, objctf_content, duree_min) FROM stdin;
1	1	1	2	Présentation du marché de la restauration à Madagascar 	2
3	1	1	4	Importance de l'expérience client, surtout dans un contexte où elle peut être nouvelle pour certains employés	2
5	1	1	6	 Gestion des imprévus (coupures d'électricité, pénuries d'eau)	2
7	1	1	8	Adaptation au coût des produits importés et utilisation des produits locaux.	2
\.


--
-- Data for Name: posts_offers; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_offers (id, off, title, subtitle, price, "desc", button_text, small_desc, active, button_url) FROM stdin;
\.


--
-- Data for Name: posts_promocode; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_promocode (id, code, valid_from, valid_to, active, amount) FROM stdin;
\.


--
-- Data for Name: posts_order; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_order (id, ordered, created, user_id, phone, coupon_id, "emailAddress", total, order_id, payment_id) FROM stdin;
\.


--
-- Data for Name: posts_order_orderitems; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_order_orderitems (id, order_id, cart_id) FROM stdin;
\.


--
-- Data for Name: posts_paiement; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_paiement (transaction_id, ref_transact, sender, receiver, transact_type, remarque, formation_id_id, matricule_id, montant, date_paiement) FROM stdin;
6	1234	0348734554	0346765567	mvola	test 5	business	4	100000	2024-04-07
7	1234567	0348734554	0346765567	mvola	ceci est juste un test pour vérifier l'automatisation du vérification des paiement sur les demandes d'inscriptions aux formations payantes	ab_bar	4	100000	2024-04-07
\.


--
-- Data for Name: posts_partenaires; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_partenaires (id, nom, logo, partner_id, "Description") FROM stdin;
1	TUMBU	images/logo_tumbu.jpg	1	Agence de formation ayant pour objectif d’aider les futurs professionnels de l’événementiel, de l’hôtellerie, de la restauration et des métiers de service à montrer ce que Madagascar a de meilleur à offrir.
2	MIARY DIGITAL	images/logo_miary.png	2	Il s’agit d’un programme d’incubation et d’attribution de subventions à des porteurs de projet et des startups entrepreneurs du secteur du numérique, incubés par cohortes.
3	ZAFY TODY	images/logo_zafitody.jpg	3	Incubateur pro-bono spécialisé dans l’accompagnement des startups tech à Madagascar, proposant un service d’incubation “end-to-end”.
\.


--
-- Data for Name: posts_post_maincourse; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_post_maincourse (id, post_id, maincourse_id) FROM stdin;
\.


--
-- Data for Name: posts_quizz; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_quizz (id, chap_id, frmt_id, quizz_id, question, qst_type, answer, status) FROM stdin;
\.


--
-- Data for Name: posts_reviews; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_reviews (id, content, stars, created, post_id, user_id) FROM stdin;
\.


--
-- Data for Name: posts_souscription_atelier; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_souscription_atelier (souscription_id, date_inscription, atelier_id_id, matricule_id, priority) FROM stdin;
17	2024-08-03	4	4	1
23	2024-08-31	1	4	1
\.


--
-- Data for Name: posts_souscription_formation; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_souscription_formation (dmd_souscription_id, operator, ref_transact, souscription_status, date_souscription, date_modification, formation_id_id, matricule_id) FROM stdin;
12	orange_money	jH876sdf	Waiting	2024-04-13	2024-04-20	business	17
13	airtel_money	09lkjbj234	Waiting	2024-04-13	2024-04-20	ab_bar	17
7	mvola	1234	Validated	2024-04-06	2024-04-20	business	4
9	mvola	1234567	Denied	2024-04-07	2024-04-20	ab_bar	4
10	mvola	4567654	Validated	2024-04-13	2024-04-20	business	18
11	mvola	987890	Denied	2024-04-13	2024-04-27	ab_bar	18
14	mvola	0987654321	Waiting	2024-08-31		form_test	18
\.


--
-- Data for Name: posts_student_progess; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_student_progess (matricule, chap_id, frmt_id, status) FROM stdin;
\.


--
-- Data for Name: posts_tcforblog; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_tcforblog (id, title, content, blank_page_id) FROM stdin;
\.


--
-- Data for Name: posts_timing; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_timing (id, date, day_duration, time_duration1, time_duration2, "Post_id") FROM stdin;
\.


--
-- Data for Name: posts_video; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_video (id, title, serial_number, video_id, is_preview, "desc", post_id) FROM stdin;
\.


--
-- Data for Name: posts_video_chap; Type: TABLE DATA; Schema: public; Owner: tumbu
--

COPY public.posts_video_chap (video_id, chap_id_id, formation_id_id, cours_content, date_creation, description, duree_min, exemple_content, "order", titre) FROM stdin;
2	8	rest_mada	formations/cours/Ch1 - 1.mp4	2024-06-22 08:49:15.03091+00	un petit descr	UNDEFINED	UNUPLOADED	0	un petit test
3	8	rest_mada	formations/cours/Ch1 - 2.mp4	2024-06-22 09:02:29.823213+00	simple descr	UNDEFINED	UNUPLOADED	0	chapitre 1.2
8	10	rest_mada	formations/cours/Chap 3 - 1.mp4	2024-06-22 09:43:53.595937+00	descr	UNDEFINED	UNUPLOADED	0	chap 3.1
10	11	rest_mada	formations/cours/Chap 4 - 1.mp4	2024-06-22 10:58:07.679724+00	descr	UNDEFINED	UNUPLOADED	0	chap 4.1
11	11	rest_mada	formations/cours/Chap 4 - 2.mp4	2024-06-22 10:58:36.147648+00	tets	UNDEFINED	UNUPLOADED	0	chap 4.2
12	12	rest_mada	formations/cours/Cha 5 - 1.mp4	2024-06-22 10:59:08.788457+00	descr	UNDEFINED	UNUPLOADED	0	chap 5.1
13	12	rest_mada	formations/cours/Cha 5 - 2.mp4	2024-06-22 10:59:39.067642+00	descr	UNDEFINED	UNUPLOADED	0	chap 5.2
14	9	rest_mada	formations/cours/Chap 2 - 1.mp4	2024-06-22 13:06:31.702628+00	une petite description	UNDEFINED	UNUPLOADED	0	chap 2.1
15	9	rest_mada	formations/cours/Chap 2 - 2.mp4	2024-06-22 13:07:05.515173+00	encore une autre description	UNDEFINED	UNUPLOADED	0	chap 2.2
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 188, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 19, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 46, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 239, true);


--
-- Name: posts_answer_possible_answer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_answer_possible_answer_id_seq', 33, true);


--
-- Name: posts_atelier_atelier_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_atelier_atelier_id_seq', 7, true);


--
-- Name: posts_blank_page_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_blank_page_id_seq', 1, false);


--
-- Name: posts_blog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_blog_id_seq', 1, false);


--
-- Name: posts_boxes_three_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_boxes_three_id_seq', 1, false);


--
-- Name: posts_cart_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_cart_id_seq', 1, false);


--
-- Name: posts_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_category_id_seq', 1, false);


--
-- Name: posts_certificate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_certificate_id_seq', 1, false);


--
-- Name: posts_chapitre_chap_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_chapitre_chap_id_seq', 5, true);


--
-- Name: posts_clients_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_clients_id_seq', 1, false);


--
-- Name: posts_collabo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_collabo_id_seq', 1, false);


--
-- Name: posts_comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_comment_id_seq', 1, false);


--
-- Name: posts_curriculam_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_curriculam_id_seq', 1, false);


--
-- Name: posts_demande_inscription_dmd_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_demande_inscription_dmd_id_seq', 29, true);


--
-- Name: posts_faq_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_faq_id_seq', 1, false);


--
-- Name: posts_features_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_features_id_seq', 1, false);


--
-- Name: posts_maincourse_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_maincourse_id_seq', 1, false);


--
-- Name: posts_notes_note_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_notes_note_id_seq', 4, true);


--
-- Name: posts_offers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_offers_id_seq', 1, false);


--
-- Name: posts_ojectif_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_ojectif_id_seq', 8, true);


--
-- Name: posts_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_order_id_seq', 1, false);


--
-- Name: posts_order_orderitems_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_order_orderitems_id_seq', 1, false);


--
-- Name: posts_paiement_transaction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_paiement_transaction_id_seq', 7, true);


--
-- Name: posts_partenaires_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_partenaires_id_seq', 1, false);


--
-- Name: posts_post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_post_id_seq', 1, false);


--
-- Name: posts_post_maincourse_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_post_maincourse_id_seq', 1, false);


--
-- Name: posts_promocode_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_promocode_id_seq', 1, false);


--
-- Name: posts_question_question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_question_question_id_seq', 15, true);


--
-- Name: posts_quizz_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_quizz_id_seq', 1, false);


--
-- Name: posts_reviews_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_reviews_id_seq', 1, false);


--
-- Name: posts_souscription_atelier_souscription_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_souscription_atelier_souscription_id_seq', 23, true);


--
-- Name: posts_souscription_formation_dmd_souscription_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_souscription_formation_dmd_souscription_id_seq', 16, true);


--
-- Name: posts_student_progess_chap_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_student_progess_chap_id_seq', 1, false);


--
-- Name: posts_subcat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_subcat_id_seq', 1, false);


--
-- Name: posts_tcforblog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_tcforblog_id_seq', 1, false);


--
-- Name: posts_timing_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_timing_id_seq', 1, false);


--
-- Name: posts_utilisateur_matricule_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_utilisateur_matricule_seq', 8, true);


--
-- Name: posts_video_chap_video_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_video_chap_video_id_seq', 15, true);


--
-- Name: posts_video_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tumbu
--

SELECT pg_catalog.setval('public.posts_video_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

