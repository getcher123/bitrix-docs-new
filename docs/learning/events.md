# События


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| **OnBeforeCertificateAdd** | перед добавлением сертификата | CAllCertification::Add | 12.0 |
| **OnAfterCertificateAdd** | после добавления сертификата | CAllCertification::Add | 12.0 |
| **OnBeforeCertificateUpdate** | перед изменением сертификата | CAllCertification::Update | 12.0 |
| **OnAfterCertificateUpdate** | после изменения сертификата | CAllCertification::Update | 12.0 |
| **OnBeforeCertificateDelete** | перед удалением сертификата | CAllCertification::Delete | 12.0 |
| **OnAfterCertificateDelete** | после удаления сертификата | CAllCertification::Delete | 12.0 |
| **OnBeforeCertificate** | перед сертификацией | CAllCertification::Certificate | 12.0 |
| **OnBeforeLessonAdd** | перед добавлением курса/главы/урока Отличить курс от урока поможет условие `$lesson["LINKED_LESSON_ID"] > 0` | CLearnLesson::Add | 12.0 |
| **OnAfterLessonAdd** | после добавления курса/главы/урока | CLearnLesson::Add | 12.0 |
| **OnBeforeLessonUpdate** | перед изменением курса/главы/урока | CLearnLesson::Update | 12.0 |
| **OnAfterLessonUpdate** | после изменения курса/главы/урока | CLearnLesson::Update | 12.0 |
| **OnBeforeLessonDelete** | перед удалением курса/главы/урокаCLearnLesson::Delete 12.0 | CLearnLesson::Delete | 12.0 |
| **OnAfterLessonDelete** | после удаления курса/главы/урока | CLearnLesson::Delete | 12.0 |
| **OnBeforeStudentAdd** | перед добавлением учетной записи студента | CStudent::Add | 12.0 |
| **OnAfterStudentAdd** | после добавления учетной записи студента | CStudent::Add | 12.0 |
| **OnBeforeStudentUpdate** | перед изменением учетной записи студента | CStudent::Update | 12.0 |
| **OnAfterStudentUpdate** | после изменения учетной записи студента | CStudent::Update | 12.0 |
| **OnBeforeStudentDelete** | перед удалением учетной записи студента | CStudent::Delete | 12.0 |
| **OnAfterStudentDelete** | после удаления учетной записи студента | CStudent::Delete | 12.0 |
| **OnBeforeTestAdd** | перед добавлением теста | CTest::Add | 12.0 |
| **OnAfterTestAdd** | после добавления теста | CTest::Add | 12.0 |
| **OnBeforeTestUpdate** | перед изменением теста | CTest::Update | 12.0 |
| **OnAfterTestUpdate** | после изменения теста | CTest::Update | 12.0 |
| **OnBeforeTestDelete** | перед удалением теста | CTest::Delete | 12.0 |
| **OnAfterTestDelete** | после удаления теста | CTest::Delete | 12.0 |
| **OnAfterQuestionAdd** | после добавления вопроса | CLQuestion::Add | 12.0 |
| **OnAfterQuestionUpdate** | после обновления вопроса | CLQuestion::Update | 12.0 |
| **OnAfterQuestionDelete** | после удаления вопроса | CLQuestion::Delete | 12.0 |
| **OnAfterAttemptFinished** | после завершения попытки прохождения теста | CAllTestAttempt::AttemptFinished | 12.0 |
| **OnBeforeLearningGroupAdd** | перед добавлением учебной группы | CLearningGroup::add | 12.0 |
| **OnAfterLearningGroupAdd** | после добавления учебной группы | CLearningGroup::add | 12.0 |
| **OnBeforeLearningGroupUpdate** | перед обновлением учебной группы | CLearningGroup::update | 12.0 |
| **OnAfterLearningGroupUpdate** | после обновления учебной группы | CLearningGroup::update | 12.0 |
| **OnBeforeLearningGroupDelete** | перед удалением учебной группы | CLearningGroup::delete | 12.0 |
| **OnAfterLearningGroupDelete** | после удаления учебной группы | CLearningGroup::delete | 12.0 |
| **OnAfterLearningGroupMemberAdd** | после добавления члена учебной группы | CLearningGroupMember::add | 12.0 |
